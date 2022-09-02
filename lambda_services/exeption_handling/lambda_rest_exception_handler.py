import json
from exeption_handling.lambda_exceptions import BadRequestException, InternalServerError
from json import JSONEncoder


class Encoder(JSONEncoder):
        def default(self, obj):
            return obj.__dict__


def request_wrapper_with_patial(func):
    try:
        pay_load, status_code = func()
    except BadRequestException as e:
        pay_load = {'error': e,
                    }
        status_code = 400
    except InternalServerError as e:
        pay_load = {'error': e,
                    }
        status_code = 502
    return {"statusCode": status_code,
                "body": json.dumps(pay_load, cls=Encoder)
            }


