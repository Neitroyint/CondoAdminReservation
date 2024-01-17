import simplejson
from flask_marshmallow import Marshmallow

from model.marshmallow_init import MarshmallowInit
from model.user.user_model import User
from schemas.user_info.user_info_schema import UserinfoSchema
from schemas.user_status.user_status_schema import UserstatusSchema

ma_initialization = MarshmallowInit.instance()
ma: Marshmallow = ma_initialization.ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        json_module = simplejson
        include_fk = False
        include_relationships = True
    
    userinfo = ma.Nested(UserinfoSchema, many=False) 
    userstatus = ma.Nested(UserstatusSchema, many=False) 