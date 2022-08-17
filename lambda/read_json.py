import json
from errors import Error
def read_json(event):
    get_value(event, "path")
    print('request: {}'.format(json.dumps(event)))


def get_value(data, key) -> any:
    Error.check_value(data, key)
    return data[key]