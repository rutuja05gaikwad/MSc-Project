
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ssm_client = boto3.client('ssm')
    
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']

    command = f'/home/ubuntu/scan_and_clean.sh {s3_bucket} {s3_key}'

    logger.info(f"Command to be sent: {command}")

    response = ssm_client.send_command(
        InstanceIds=['i-00d70d6b4285473f6'],
        DocumentName="AWS-RunShellScript",
        Parameters={'commands': [command]},
        TimeoutSeconds=60
    )

    command_id = response['Command']['CommandId']
    logger.info(f"SSM Command ID: {command_id}")

    return {'statusCode': 200, 'body': json.dumps('Command sent to EC2')}
