import boto3
import json
import time

# Initialize Boto3 clients
s3_client = boto3.client('s3')
lambda_client = boto3.client('lambda')

# Variables
bucket_name = 'securefileclamav'
lambda_function_name = 'clamavlambda'

def get_lambda_function_arn(function_name):
    """Retrieve the ARN of a Lambda function."""
    response = lambda_client.get_function(FunctionName=function_name)
    return response['Configuration']['FunctionArn']

def create_s3_bucket():
    """Create an S3 bucket."""
    try:
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
            'LocationConstraint': 'us-west-1'
        })
        print(f"S3 bucket '{bucket_name}' created successfully.")
    except s3_client.exceptions.BucketAlreadyExists:
        print(f"S3 bucket '{bucket_name}' already exists.")
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")

def configure_s3_event_notification(bucket_name, lambda_arn):
    s3_client = boto3.client('s3')

    notification_configuration = {
        'LambdaFunctionConfigurations': [
            {
                'LambdaFunctionArn': lambda_arn,
                'Events': ['s3:ObjectCreated:*'],
                'Filter': {
                    'Key': {
                        'FilterRules': [
                            {
                                'Name': 'suffix',
                                'Value': '.zip'
                            }
                        ]
                    }
                }
            }
        ]
    }

    try:
        s3_client.put_bucket_notification_configuration(
            Bucket=bucket_name,
            NotificationConfiguration=notification_configuration
        )
        print(f"S3 event notification configured for bucket '{bucket_name}' with Lambda ARN '{lambda_arn}'")
    except Exception as e:
        print(f"An error occurred while configuring S3 event notification: {e}")

def main():
    # Create the S3 bucket
    create_s3_bucket()
    
    # Retrieve the Lambda function ARN
    lambda_arn = get_lambda_function_arn(lambda_function_name)
    
    # Wait a few seconds to ensure the Lambda function is fully set up
    time.sleep(10)
    
    # Configure S3 event notification
    configure_s3_event_notification(lambda_arn)

if __name__ == "__main__":
    main()
