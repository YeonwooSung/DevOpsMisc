# Elastic Container Registry (ECR)

Amazon Elastic Container Registry (Amazon ECR) is an AWS managed container image registry service that is secure, scalable, and reliable.
Amazon ECR supports private repositories with resource-based permissions using AWS IAM.
This is so that specified users or Amazon EC2 instances can access your container repositories and images.
You can use your preferred CLI to push, pull, and manage Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts.

## Login docker into ECR repo

To upload/download images into/from ECR repositories, you need to log in to the target ECR repo.
You could do this with AWS-cli and docker by using command below:

```
$ aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
```

For example, if you want to log in to the `763104351884.dkr.ecr.us-east-1.amazonaws.com` repository that is published on the us-east-1, run the following command:

```
$ aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-east-1.amazonaws.com
```

### Pull SageMaker PyTorch 1.12.1 image from ECR

```
# login ECR with docker
$ aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.ap-northeast-2.amazonaws.com

# pull sagemaker pytorch 1.12.1 image from ECR repo
$ docker pull 763104351884.dkr.ecr.ap-northeast-2.amazonaws.com/pytorch-inference:1.12.1-cpu-py38-ubuntu20.04-sagemaker-v1.6
```
