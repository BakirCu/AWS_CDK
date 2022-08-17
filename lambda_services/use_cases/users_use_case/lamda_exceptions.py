
class BadRequestException(Exception):
    
    @staticmethod
    def raise_erorr(error):
        return {"statusCode":400,
                "body":error}


class NotFoundException(Exception):
    pass                


class InputError(Exception):
    pass