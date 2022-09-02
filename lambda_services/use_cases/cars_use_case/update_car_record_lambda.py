import logging
from exeption_handling.lambda_rest_exception_handler import request_wrapper_with_patial
from providers import user_repository
import lambda_helpers.lambda_path_parametars_helper as path
import lambda_helpers.lambda_body_parametars_helper as body
from genaral_helpers.maper import user_entity_to_dto
from functools import partial


LOG = logging.getLogger() 
LOG.setLevel(logging.INFO)


def lambda_handler(event, context):
    LOG.info(event)
    car_properties= body.get_body_value("body", event)
    user_id = path.get_id_value(key= 'user_id', param_key='pathParameters',data= event)
    car_id = path.get_id_value(key= 'car_id', param_key='pathParameters',data= event)
    
    lambda_service_calable = partial(lambda_service, user_id, car_id, car_properties)
    return request_wrapper_with_patial(lambda_service_calable)
   
   
def lambda_service(user_id, car_id, car_properties):
    user_entity = user_repository.get_by_id(user_id)
    user_dto = user_entity_to_dto(user_entity)
    user_dto.add_car(car_id, car_properties["type"])
    cars_dto = user_dto.get_cars()
    user_repository.add_atribute(user_id, "cars", [car.__dict__ for car in cars_dto])
    return cars_dto, 200