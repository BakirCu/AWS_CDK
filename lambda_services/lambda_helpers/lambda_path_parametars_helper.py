from exeption_handling.lambda_exceptions import InputException


def get_id_value( key: str, param_key: str, data: dict) -> int:
    params = data.get(param_key)
    if not params:
        raise InputException(f"Plese provide value od {key}, params can't be {params}")

    value = params.get(key)
    if not value:
        raise InputException(f"Params: {params} must contains key: {key}")

    try:
        id = int(value)
    except ValueError as error:
        raise InputException("Value of user_id must be an integer: {error}")
        
    return id
