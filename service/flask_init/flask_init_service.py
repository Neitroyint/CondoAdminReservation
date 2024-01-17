from flask import Flask
from werkzeug.exceptions import InternalServerError
from utils.constants import env_const
from utils.decorators.singleton_decorator import Singleton
from utils.responses.https_response import HttpResponse

@Singleton
class FlaskInit:
    jwt: Flask
    def __init__(self) -> None:
        self.app = Flask(__name__)
        #Configuration params
        self.app.config["DEBUG"] = env_const.IS_DEBUG
        
        # FlaskErrorHandler()
        @self.app.errorhandler(InternalServerError)
        def handle_exception(e):
            return HttpResponse.InternalErrorResponse("There was an error in the request. Please contact support.").respond()
        