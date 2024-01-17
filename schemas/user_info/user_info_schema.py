from flask_marshmallow import Marshmallow

from model.marshmallow_init import MarshmallowInit
from model.user_info.user_info_model import Userinfo
from schemas.identification.identification_schema import IdentificationSchema

ma_initialization = MarshmallowInit.instance()
ma: Marshmallow = ma_initialization.ma

class UserinfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Userinfo
        include_fk = True
        include_relationships = True
        
    identification = ma.Nested(IdentificationSchema, many=False) 