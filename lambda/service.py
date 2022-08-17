import boto3

class DynamoDbService:
    def __init__(self, dynamodb=None):
        if not dynamodb:
            self.dynamodb = boto3.resource('dynamodb')

    def get_item(self, table_name, params: dict):
        return self.dynamodb.get_item(
            TableName=table_name,
            Key=params
        #     Key={
        #         'artist': {'S': 'Arturus Ardvarkian'},
        #         'song': {'S': 'Carrot Eton'}
        #     }
        )
    def put_item(self, table_name, params: dict):
        pass