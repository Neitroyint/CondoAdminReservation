from flask_restful import Resource

from utils.constants import endpoint_routes
from utils.responses.https_response import HttpResponse

class StatusController(Resource):
    route = endpoint_routes.STATUS_ROUTE

    @staticmethod
    def get():
        return HttpResponse.SuccessResponse('Hello There! Come here my little friend').respond()
