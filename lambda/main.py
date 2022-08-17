import json
from create_table import create_movie_table
from read_json import read_json
from service import DynamoDbService
def main(event, context):
    # create_movie_table()
    read_json(event)

    if event["httpMethod"] == "POST":
        DynamoDbService.put_item()
        
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
    }

# main({"pat":"saas"},'sda')