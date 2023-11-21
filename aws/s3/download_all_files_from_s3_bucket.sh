
BUCKET_NAME="mybucket"

# Download all files from S3 bucket
aws s3 sync s3://$BUCKET_NAME .
