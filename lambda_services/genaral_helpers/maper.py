from use_cases.users_use_case.user_dto import UserDto
from data_access.entity.user_entity import UserEntity


user_entity_to_dto = lambda entity,: UserDto(int(entity.id), entity.username, entity.password, entity.country, entity.cars)


dto_to_entity = lambda dto : UserEntity(dto.id, dto.username, dto.password, dto.country, dto.cars)


def list_to_list_maper(list, maper_lambda):
    return map(maper_lambda, list)



