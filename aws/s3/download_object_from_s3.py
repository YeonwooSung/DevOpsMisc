import boto3

s3_client = boto3.client('s3')

def get_video_from_s3(s3_bucket, s3_key, file_path):
    """Get video from S3 bucket

    Args:
        s3_bucket (str): S3 bucket name
        s3_key (str): S3 key
        file_path (str): File path to save the video

    Returns:
        bytes: Video bytes
    """
    # Download the video file from S3 bucket
    with open(file_path, 'wb') as data:
        s3_client.download_fileobj(s3_bucket, s3_key, data)
