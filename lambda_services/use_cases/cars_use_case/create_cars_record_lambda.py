import logging
from exeption_handling.lambda_rest_exception_handler import request_wrapper_with_patial
from providers import user_repository
import lambda_helpers.lambda_path_parametars_helper as path
import lambda_helpers.lambda_body_parametars_helper as body
from functools import partial


LOG = logging.getLogger() 
LOG.setLevel(logging.INFO)


def lambda_handler(event, context):
    cars_dict = body.get_body_value("body", event)
    cars = cars_dict.get('cars')
    user_id = path.get_id_value(key= 'user_id', param_key='pathParameters',data= event)
    lambda_service_calable = partial(lambda_service, user_id, cars)
    return request_wrapper_with_patial(lambda_service_calable)
   
   
def lambda_service(user_id, atribute):
    user_repository.add_atribute(user_id, "cars", atribute)
    return atribute, 200