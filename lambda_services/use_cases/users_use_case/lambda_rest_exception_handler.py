from lamda_exceptions import BadRequestException, NotFoundException
from providers import db_provider


def request_wrapper(func, event, context):
    try:
        data = func(event, context)
    except BadRequestException: # how python knows when to trow this exeption?
        BadRequestException.raise_erorr("something")
    except NotFoundException:
        return {"statusCode": 404}
    except TypeError: # this is ok
        return 'wrong type of atribute'
    # some exception handling such as
    # if BadREquestException => return http 400
    # if NotFoundException => return http 404
    # for others => return 500
    return data


def is_valid(value):
    record = db_provider.get_by_id(value)
    if record or isinstance(value, int):
        return True
    return False