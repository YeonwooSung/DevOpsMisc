import json
import boto3
import os
import io
from PIL import Image


s3_client = boto3.client("s3")
s3_connection = boto3.resource('s3')
sage_client = boto3.client('sagemaker-runtime')
threshold = 0.6


def detect_faces_sagemaker(sage_client, image_obj):
    response = sage_client.invoke_endpoint(
        EndpointName='your endpoint name',
        Body=image_obj,
        ContentType='image/jpeg',
        Accept='json'
    )
    result = json.loads(response['Body'].read().decode())
    faces = False
    for pred_item in result["prediction"]:
        if pred_item[0] == 0 and pred_item[1] >= threshold:
            print("person identified")
            faces = True
            break
    return faces


def lambda_handler(event, context):
    target_bucket = "your target bucket"
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    s3_object = s3_connection.Object(bucket,key)
    s3_response = s3_object.get()

    stream = io.BytesIO(s3_response['Body'].read())

    image=Image.open(stream)
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()

    faces = detect_faces_sagemaker(sage_client, imgByteArr)

    if faces:
        copy_source = {
        'Bucket': bucket, 
        'Key': key
    }
        s3_client.copy(copy_source,target_bucket,key)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
