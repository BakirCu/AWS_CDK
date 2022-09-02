from exeption_handling.lambda_exceptions import InputException
import json


def get_body_value(key: str, data: dict)-> dict:
    value = data.get(key)
    if not value:
        raise InputException("Body is empty")    
    return json.loads(value)

