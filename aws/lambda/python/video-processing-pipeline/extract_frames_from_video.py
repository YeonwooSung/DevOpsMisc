import boto3
import cv2
import io
import json
from PIL import Image
import tempfile


def lambda_handler(event, context):
    s3_target_bucket = "target_bucket_name"
    dir_path = "/tmp/"
    s3_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]
    file_name = "name of your file"

    s3_client = boto3.client('s3')

    with open("/tmp/{}".format(file_name), 'wb') as data:
        s3_client.download_fileobj(s3_bucket, key, data)
    cap = cv2.VideoCapture("/tmp/{}".format(file_name))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    for fno in range(0, total_frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, fno)
        _, frame = cap.read()

        img = Image.fromarray(frame)
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format='JPEG')
        imgByteArr = imgByteArr.getvalue()

        im_name = "name of the image file"

        with tempfile.NamedTemporaryFile(mode="wb", delete="True") as jpg:
            jpg.write(imgByteArr)
            s3_client.upload_file(jpg.name, s3_target_bucket, im_name)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
