import logging
from exeption_handling.lambda_rest_exception_handler import request_wrapper_with_patial
from providers import user_repository
import lambda_helpers.lambda_path_parametars_helper as path
from exeption_handling.lambda_rest_exception_handler import BadRequestException
from functools import partial


LOG = logging.getLogger() 
LOG.setLevel(logging.INFO)


def lambda_handler(event, context):
    user_id = path.get_id_value(key= 'user_id', param_key='pathParameters',data= event)
    user = user_repository.get_by_id(user_id)
    if user:
        cars = []
        lambda_service_calable = partial(lambda_service, user.get_id(), cars)
        return request_wrapper_with_patial(lambda_service_calable)
    raise BadRequestException("User don't exist")
   
   
def lambda_service(user_id, atribute):
    user_repository.add_atribute(user_id, "cars", atribute)
    return atribute, 200

