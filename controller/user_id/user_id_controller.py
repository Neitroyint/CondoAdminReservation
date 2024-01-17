import json
from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from model.user.user_model import User
from schemas.requests_schemas.profile_schema import ProfilePutSchema
from service.profile.profile_service import ProfileService
from schemas.user.user_schema import UserSchema
from utils.decorators.authentication_decorator import auth_required
from utils.constants import endpoint_routes
from utils.responses.https_response import HttpResponse


class UserIdController(Resource):
    route = endpoint_routes.USER_ID_ROUTE

    method_decorators = {
        'get': [auth_required("ADMINISTRADOR")],
        'put': [auth_required("ADMINISTRADOR")],
    }

    @staticmethod
    def get(id):
        try:
            user = User.query.get(id)
            if user is None:
                return 
            data = UserSchema().dumps(user)
            return HttpResponse.SuccessResponse("User retrieved successfully", {"user": json.loads(data)}).respond()
        except:
            return HttpResponse.InternalErrorResponse("Error executing the request").respond()

    @staticmethod
    def put(id):
        try:
            profile = ProfilePutSchema().load(request.json)
            user = ProfileService.update_profile(id, profile)
            if user is None:
                return HttpResponse.NotFoundResponse("User not found").respond()
            data = UserSchema().dumps(user)
            return HttpResponse.SuccessResponse("Users retrieved successfully", {"users": json.loads(data)}).respond()
        except ValidationError as v_err:
            return HttpResponse.BadRequestResponse(v_err.messages)
        except Exception as err:
            return HttpResponse.InternalErrorResponse("Error executing the request").respond()
        except BaseException as err:
            return HttpResponse.InternalErrorResponse(err.args[0]).respond()


