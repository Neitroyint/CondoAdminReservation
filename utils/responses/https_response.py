import json
from typing import Any

from flask.json import jsonify
from flask import make_response


class HttpResponse():
    def __init__(self, data: Any = None, message: str = "", status: int = "") -> None:
        self.data = data
        self.message = message
        self.status = status

    @classmethod
    def SuccessResponse(cls, message: str, data = None):
        suc = cls(message=message, status=200)
        if data != None:
            if type(data) == str:
                suc.data = json.loads(data)
            else:
                suc.data = data
        return suc

    @classmethod
    def BadRequestResponse(cls, message: str):
        return cls(message=message, status=400)

    @classmethod
    def UnauthorizedResponse(cls, message: str):
        return cls(message=message, status=401)

    @classmethod
    def NotFoundResponse(cls, message: str):
        return cls(message=message, status=404)

    @classmethod
    def InternalErrorResponse(cls, message: str):
        return cls(message=message, status=500)

    def respond(self) -> tuple[str, int]:
        data = self.json()
        return make_response(data, self.status) 

    def json(self) -> str:
        data = {
            "message": self.message
        }
        if self.data != None:
            data["data"] = self.data
        return jsonify(data)

    