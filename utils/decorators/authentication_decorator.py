import requests
from flask_restful import request
from functools import wraps

from utils.constants import env_const
from utils.responses.https_response import HttpResponse

def auth_required(permission):
    def decorator(f):
        @wraps(f)
        def catcher(*args, **kwargs):
            try:
                token = request.headers["Authorization"]
            except:
                return HttpResponse.UnauthorizedResponse("Invalid Token").respond()
            try:
                req_header = {
                    "Authorization": f"JWT {token}"
                }
                body = {
                    'permission': permission
                }
                response = requests.post(env_const.AUTH_URL, json=body, headers=req_header, timeout=20)
            except:
                return HttpResponse.InternalErrorResponse("Unable to authenticate. Please contact support.").respond()
            if response.status_code == 200:
                return f(*args, **kwargs)
            else:
                return HttpResponse.UnauthorizedResponse("Unauthorized").respond()
        return catcher
    return decorator