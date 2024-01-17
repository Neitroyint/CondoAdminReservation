import simplejson
from flask_marshmallow import Marshmallow

from model.marshmallow_init import MarshmallowInit
from model.user_status.user_status_model import Userstatus

ma_initialization = MarshmallowInit.instance()
ma: Marshmallow = ma_initialization.ma

class UserstatusSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Userstatus
        json_module = simplejson
        include_fk = False