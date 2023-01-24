import boto3
import cv2
import io
import json
from PIL import Image
import tempfile
import uuid


def lambda_handler(event, context):
    s3_target_bucket = "target_bucket_name"

    # Generate a unique ID for the video file
    my_uuid = str(uuid.uuid4())

    # Get event record, where the event is the "Put" event on the S3 bucket
    s3_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]
    file_name = f"temp_{my_uuid}.mp4"
    tmp_file_path = f"/tmp/{file_name}"

    s3_client = boto3.client('s3')

    # Download the video file from S3 bucket
    with open(tmp_file_path, 'wb') as data:
        s3_client.download_fileobj(s3_bucket, key, data)

    # Open the video file
    cap = cv2.VideoCapture(tmp_file_path)

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # Get the frame rate of the video
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # Set the sampling rate by using fps
    eval_step = fps

    for fno in range(0, total_frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, fno)
        ret, frame = cap.read()
        # break if no frame is returned
        if not ret:
            break
        # skip frames to sample frames as per fps
        if fno % eval_step != 0 and fno != 1:
            continue

        # Use try-except block to handle any errors
        # Also, by using this try-except block, we could skip the frame if there is an error.
        # This means that even if there is an error in one frame, we could still process the rest of the frames.
        try:
            img = Image.fromarray(frame)
            imgByteArr = io.BytesIO()
            img.save(imgByteArr, format='JPEG')
            imgByteArr = imgByteArr.getvalue()

            # Set the image name with the unique ID and frame number
            im_name = f"{my_uuid}_{fno}.jpg"
            # Upload the image to S3 bucket
            with tempfile.NamedTemporaryFile(mode="wb", delete="True") as jpg:
                jpg.write(imgByteArr)
                s3_client.upload_file(jpg.name, s3_target_bucket, im_name)
        except:
            print("Error in uploading image to S3 bucket")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
