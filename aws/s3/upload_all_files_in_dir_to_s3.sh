
BUCKET_NAME="mybucket"

# Upload all files to S3 bucket
aws s3 sync . s3://$BUCKET_NAME
