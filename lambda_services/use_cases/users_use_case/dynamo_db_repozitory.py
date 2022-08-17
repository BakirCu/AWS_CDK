import boto3
from base_repository import BaseRepository


class DynamoDBRepository(BaseRepository):

    dynamo_db_resource = boto3.resource('dynamodb')

    def __init__(self, table_name) -> None:
        self.table = DynamoDBRepository.dynamo_db_resource.Table(table_name) 

    def get_all(self):
        return self.table.scan()

    def get_by_id(self, id):
        return self.table.get_item(Key = {"id": id})

    def create(self, record):
        self.table.put_item(Item=record)