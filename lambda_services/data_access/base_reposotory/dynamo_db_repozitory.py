import boto3
from data_access.base_reposotory.base_repository import BaseRepository


class DynamoDBRepository(BaseRepository):

    dynamo_db_resource = boto3.resource('dynamodb')

    def __init__(self, table_name) -> None:
        self.table = DynamoDBRepository.dynamo_db_resource.Table(table_name) 

    def get_all(self):
        return self.table.scan()

    def get_by_id(self, id: int):
        res = self.table.get_item(Key= {"id": id})
        return res
        
    def create(self, record: dict):
        self.table.put_item(Item= record)

    def update(self, id: int, username: str, password: str):
        response = self.table.update_item(
            Key={'id': id},
            UpdateExpression="set username=:r, password=:p",
            ExpressionAttributeValues={
                ':r': username, ':p': password},
            ReturnValues="UPDATED_NEW")
        return response['Attributes']
   
    def delete_by_id(self, id: int):
        self.table.delete_item(Key= {"id": id})
        return f"User id: {id} deleted" 
    
    def add_atribute(self, id: int, atribute_name: str,  atribute_value: str):
        response = self.table.update_item(
            Key= {'id': id},
            UpdateExpression= f"set {atribute_name}=:r",
            ExpressionAttributeValues= {':r': atribute_value },
            ReturnValues= "UPDATED_NEW")
        return response['Attributes']