# Reference: <https://medium.com/swlh/upload-binary-files-to-s3-using-aws-api-gateway-with-aws-lambda-2b4ba8c70b8e>

import json
import base64
import boto3


BUCKET_NAME = 'YOUR_S3_BUCKET_NAME_HERE'

def lambda_handler(event, context):
    file_content = base64.b64decode(event['content'])
    file_path = 'YOUR_FILE_PATH_HERE'
    s3 = boto3.client('s3')
    try:
        s3_response = s3.put_object(Bucket=BUCKET_NAME, Key=file_path, Body=file_content)
    except Exception as e:
        raise IOError(e)
    return {
        'statusCode': 200,
        'body': {
            'file_path': file_path
        }
    }
