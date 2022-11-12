# AWS DevOps

## Lambda codes for Cloudtrail logs to Elasticsearch

This CloudFormation template creates:

    - Multi-region CloudTrail trail
    - CloudWatch Logs log group that is the target of CloudTrail data
    - S3 Bucket that stores CloudTrail data
    - CloudWatch Logs subscription filter
    - AWS Lambda function that is target of subscription filter. Sends data to AWS Eleasticsearch
    - AWS Elasticsearch domain, target of Lambda function
    - Nginx reverse proxy (lives in your default VPC). This is the only authorized IP that can write to the Elasticsearch domain.
    - Security Group for the Nginx reverse proxy. You can configure this security group with authorized IPs to access the Nginx proxy on port 80.

1. Lambda function code - LogsToElasticsearch.js

Lambda function code that writes data to AWS Elasticsearch domain.

2. Lambda function code - UpdateElasticsearch.js

Required by CloudFormation during the stack creation. It updates the Elasticsearch cluster access policy with the IP of the Nginx reverse proxy. It also updates the code of the LogsToElasticsearch function so it points to the URL of the recently created AWS Elasticsearch cluster.

This function uses the [node-zip](https://github.com/daraosn/node-zip) module to generate .zip files that are required by Lambda when setting the function code. If you really want to modify this function, you would have to instal node-zip and create a deployment package for Lambda.
