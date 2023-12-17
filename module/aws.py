import boto3
import json


class SQS:
    def __init__(self):
        endpoint_url = "http://192.168.0.200:4566"
        sqs = boto3.resource('sqs',
                             region_name='us-east-1',
                             endpoint_url=endpoint_url,
                             aws_access_key_id="qwer",
                             aws_secret_access_key="1234"
                             )
        self.queue = sqs.get_queue_by_name(QueueName='test1')

    def consume(self):
        return self.queue.receive_messages(MaxNumberOfMessages=10)

    def produce(self, message):
        return self.queue.send_message(MessageBody=json.dumps(message))


