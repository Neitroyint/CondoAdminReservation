from utils.responses.https_response import HttpResponse

class CustomError(BaseException):
    def __init__(self, message, response, *args: object) -> None:
        super().__init__(*args)
        self.message = message
        self.response = response

    @classmethod
    def AlreadyExistsError(cls, message):
        response = HttpResponse.BadRequestResponse(message)
        return cls(message, response)
    
    @classmethod
    def NotFoundError(cls, message):
        response = HttpResponse.BadRequestResponse(message)
        return cls(message, response)

