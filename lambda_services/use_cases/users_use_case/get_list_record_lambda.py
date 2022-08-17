
from lambda_rest_exception_handler import request_wrapper
from providers import db_provider
from functools import partial


def get_all_lambda_handler(event, context):
    data = request_wrapper(get_service, event, context)
    return {
                'statusCode': 200,
                # 'body':data
            }
def get_service(event, context):
    # some business logic
    # do some validations
    # get list from DB
    # compose a nice dto
    # return the result
    data = db_provider.get_all()
    print(data)
    return data
