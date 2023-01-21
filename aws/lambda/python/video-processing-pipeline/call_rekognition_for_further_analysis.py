import json
import boto3


s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
firehose = boto3.client('firehose')

# Parameters
firehosestream = "firehose stream name"


def lambda_handler(event, context):
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    faces = rekognition.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key,
            },
        },
        Attributes=["ALL"],
    )

    id = 0
    for face in faces['FaceDetails']:
        score = 0
        best_emotion = ''
        for emotion in face['Emotions']:
            if emotion['Confidence'] > score:
                score = emotion['Confidence']
                best_emotion = emotion['Type']

        payload = {
            'faceid': id,
            'emotion': best_emotion,
            'emotionConfidence': int(score),
            'smile': face['Smile']['Value'],
            'smileConfidence': face['Smile']['Confidence'],
            'gender': face['Gender']['Value'],
            'genderConfidence': face['Gender']['Confidence'],
            'ageRangeMin': face['AgeRange']['Low'],
            'ageRangeMax': face['AgeRange']['High']
        }
        
        response = firehose.put_record(
            DeliveryStreamName=firehosestream,
            Record={
                'Data': json.dumps(payload) + '\n'
            }
        )
        id += 1
