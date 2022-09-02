import logging
from exeption_handling.lambda_rest_exception_handler import request_wrapper_with_patial
from providers import user_repository
from genaral_helpers.maper import user_entity_to_dto
import lambda_helpers.lambda_quey_parametars_helper as query
import lambda_helpers.lambda_path_parametars_helper as path
from functools import partial


LOG = logging.getLogger() 
LOG.setLevel(logging.INFO)


def lambda_handler(event, context):
    user_id = path.get_id_value(key= 'user_id', param_key='pathParameters',data= event)
    car_id = path.get_id_value(key= 'car_id', param_key='pathParameters',data= event)
    lambda_service_calable = partial(lambda_service, user_id, car_id)
    return request_wrapper_with_patial(lambda_service_calable)
  
  
def lambda_service(user_id, car_id):
    user_entity = user_repository.get_by_id(user_id)
    user_dto = user_entity_to_dto(user_entity)
    cars_dto = user_dto.get_cars()
    car_dto = query.get_car_by_id(car_id, cars_dto)
    return car_dto, 200