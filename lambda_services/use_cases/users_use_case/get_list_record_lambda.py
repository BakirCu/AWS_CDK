import logging
from exeption_handling.lambda_rest_exception_handler import request_wrapper_with_patial
from providers import user_repository
from genaral_helpers.maper import list_to_list_maper, user_entity_to_dto


LOG = logging.getLogger() 
LOG.setLevel(logging.INFO)


def lambda_handler(event, context):
    return request_wrapper_with_patial(lambda_service)


def lambda_service():
    user_etity_list = user_repository.get_all()
    user_dto_list = list(list_to_list_maper(user_etity_list, user_entity_to_dto))
    return user_dto_list, 200