from lambda_rest_exception_handler import request_wrapper, is_valid
from providers import db_provider
from lamda_exceptions import BadRequestException
from functools import partial
import json

def get_record_lambda_handler(event, context):
    data = request_wrapper(get_service, event, context)
    return {
                'statusCode': 200,
                'headers': {
            'Content-Type': 'application/json'},
                'body':'str(data["Item"])'
            }
def get_service(event, context):
    
    # some business logic
    # do some validations
    # get list from DB
    # compose a nice dto
    # return the result
    
    valid_data = json.loads(event)
    print(valid_data)
    id = valid_data['id']
    if not is_valid(id):
        raise BadRequestException("Value of 'id' must be provided as int type")
    print(id)
    data = db_provider.get_by_id(int(id))
    print(str(data["Item"]))
    return data
