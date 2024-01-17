from flask_marshmallow import Marshmallow

from model.identification.identification_model import Identification
from model.marshmallow_init import MarshmallowInit
from schemas.identification_type.identification_type_schema import IdentificationtypeSchema

ma_initialization = MarshmallowInit.instance()
ma: Marshmallow = ma_initialization.ma

class IdentificationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Identification
        include_fk = True
        include_relationships = True
        
    identificationtype = ma.Nested(IdentificationtypeSchema, many=False, required=False) 
