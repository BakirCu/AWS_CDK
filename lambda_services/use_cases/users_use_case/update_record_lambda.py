import logging
from exeption_handling.lambda_rest_exception_handler import request_wrapper_with_patial
from genaral_helpers.maper import dto_to_entity
from providers import user_repository
import lambda_helpers.lambda_body_parametars_helper as body
from use_cases.users_use_case.user_dto import UserDto
from functools import partial

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)


def lambda_handler(event, context):
    LOG.info(event)
    body_value = body.get_body_value("body", event)
    user_dto = UserDto.from_dict(body_value)
    lambda_service_calable = partial(lambda_service, user_dto)
    return request_wrapper_with_patial(lambda_service_calable)


def lambda_service(user_dto):
    user_entity = dto_to_entity(user_dto)
    user_repository.update(user_entity)
    return user_dto, 200
