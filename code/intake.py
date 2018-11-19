import json
import boto3
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sqs_client = boto3.client('sqs')

def lambda_handler(event, context):
    logger.info('got event{}'.format(event))

    responseQueueUrl = os.environ['ResponseQueueUrl']

    response = []
    for message in event['Records']:
        response.append(
            sqs_client.send_message(
                QueueUrl=responseQueueUrl,
                MessageBody=json.loads(message['body'])['message']
            )
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }