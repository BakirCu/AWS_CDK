
from imp import init_builtin
from lambda_rest_exception_handler import request_wrapper
from providers import db_provider
import json
from lamda_exceptions import InputError

def create_record_lambda_handler(event, context):
    data = request_wrapper(create_record_service, event, context)
    return {
                "statusCode": 200,
                "body":"str(data)"
            }

def create_record_service(event, context):
    data = event.get("body")
    if not data:
        raise InputError("Data must be provided in request body")
    if "id" not in data:
        raise InputError("Provide value of 'id' when create data ")
    # some business logic
    # do some validations
    # get list from DB
    # compose a nice dto
    # return the result
    # if not is_valid(record.tax_number):
    #     raise BadREquestException("The tax number {record.tax_nubmer} is not valid")
    valid_data = json.loads(data)
    db_provider.create(valid_data)
    print(valid_data)
    return data
