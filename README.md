# aws-lambda-emf-cloudformation-template

This repository contains sample CloudFormation template which will deploy a basic AWS Lambda function via AWS SAM which emits metrics using Embedded Metric Format.

## How to setup

1. Clone the repository
1. Install AWS SAM CLI https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.
html
1. Install dependencies from `requirements.txt` into `lambda_layer` via `pip install -r requirements.txt --target lambda_layer/python`
1. `sam build`
1. `sam deploy --stack-name sample-lambda`