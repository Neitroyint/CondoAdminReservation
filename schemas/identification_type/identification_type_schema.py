import simplejson
from flask_marshmallow import Marshmallow

from model.identification_type.identification_type_model import Identificationtype
from model.marshmallow_init import MarshmallowInit

ma_initialization = MarshmallowInit.instance()
ma: Marshmallow = ma_initialization.ma

class IdentificationtypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Identificationtype
        json_module = simplejson
        include_fk = False