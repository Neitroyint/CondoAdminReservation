from utils.decorators.singleton_decorator import Singleton
from flask_marshmallow import Marshmallow

@Singleton
class MarshmallowInit:
    def __init__(self) -> None:
        self.ma = Marshmallow()
    
    def init_ma(self, app) -> None:
        self.ma.init_app(app)