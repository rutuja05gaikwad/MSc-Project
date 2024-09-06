import json
import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ssm_client = boto3.client('ssm')

    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']
    instance_id = os.environ['INSTANCE_ID']

    command = f'/home/ubuntu/scan_and_clean.sh {s3_bucket} {s3_key}'
    logger.info(f"Sending command to EC2 instance {instance_id}: {command}")

    try:
        response = ssm_client.send_command(
            InstanceIds=[instance_id],
            DocumentName="AWS-RunShellScript",
            Parameters={'commands': [command]},
            TimeoutSeconds=60
        )

        logger.info(f"Command sent successfully. Command ID: {response['Command']['CommandId']}")
        return {'statusCode': 200, 'body': json.dumps('Command sent to EC2')}

    except Exception as e:
        logger.error(f"Error sending command to EC2: {e}")
        return {'statusCode': 500, 'body': json.dumps('Failed to send command to EC2')}
