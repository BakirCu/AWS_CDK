
import logging
from exeption_handling.lambda_rest_exception_handler import request_wrapper_with_patial
from providers import user_repository
from genaral_helpers.maper import user_entity_to_dto
import lambda_helpers.lambda_path_parametars_helper as path
from functools import partial


LOG = logging.getLogger() 
LOG.setLevel(logging.INFO)


def lambda_handler(event, context):
    id = path.get_id_value(key= 'user_id', param_key='pathParameters',data= event)
    lambda_service_calable = partial(lambda_service, id)
    return request_wrapper_with_patial(lambda_service_calable)
  
  
def lambda_service(id):
    user_etity = user_repository.get_by_id(id)
    user_dto = user_entity_to_dto(user_etity)
    return user_dto, 200

