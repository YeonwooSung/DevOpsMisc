import boto3

s3_client = boto3.client('s3')

def remove_video_from_s3(s3_bucket, s3_key):
    """Remove video from S3 bucket

    Args:
        s3_bucket (str): S3 bucket name
        s3_key (str): S3 key
    """
    s3_client.delete_object(Bucket=s3_bucket, Key=s3_key)
