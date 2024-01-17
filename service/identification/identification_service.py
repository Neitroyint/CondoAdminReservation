from marshmallow import EXCLUDE

from model.identification.identification_model import Identification
from schemas.identification.identification_schema import IdentificationSchema

class IdentificationService:
    @staticmethod
    def create_identification(data) -> Identification:
        ident_model = IdentificationSchema().load(data, unknown=EXCLUDE)

        if type(ident_model) is dict:
            identification = Identification(**ident_model)
        else:
            identification = ident_model

        identification.insert()
        return identification
    
    @staticmethod
    def update_identification(data, identification) -> Identification:
        ident_data = IdentificationSchema().dump(data)
        if ident_data:
            for key, value in ident_data.items():
                setattr(identification, key, value)

            identification.update()

            return identification
        else:
            return None