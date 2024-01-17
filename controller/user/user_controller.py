import json
from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from model.user.user_model import User
from schemas.requests_schemas.profile_schema import ProfilePostSchema
from schemas.user.user_schema import UserSchema
from service.profile.profile_service import ProfileService
from utils.decorators.authentication_decorator import auth_required
from utils.constants import endpoint_routes
from utils.responses.https_response import HttpResponse

class UserController(Resource):
    route = endpoint_routes.USER_ROUTE

    method_decorators = {
        'get': [auth_required("ADMINISTRADOR")],
        'post': [auth_required("ADMINISTRADOR")],
    }

    @staticmethod
    def get():
        try:
            users = User.query.all()
            data = UserSchema().dumps(users, many=True)
            if data is None or len(data) <= 0:
                return HttpResponse.NotFoundResponse("No user found.").respond()
            return HttpResponse.SuccessResponse("Users retrieved successfully.", {"users": json.loads(data)}).respond()
        except:
            return HttpResponse.InternalErrorResponse("Error executing the request").respond()

    @staticmethod
    def post():
        try:
            profile = ProfilePostSchema().load(request.json)
            user = ProfileService.create_profile(profile)
            data = UserSchema().dumps(user)
            return HttpResponse.SuccessResponse("Successsfully updated user.", {"user": json.loads(data)}).respond()
        except ValidationError as v_err:
            return HttpResponse.BadRequestResponse(v_err.messages).respond()
        except Exception as err:
            return HttpResponse.InternalErrorResponse("Error executing the request").respond()
        except BaseException as err:
            return HttpResponse.InternalErrorResponse(err.args[0]).respond()
