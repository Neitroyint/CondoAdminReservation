from marshmallow import fields, Schema

class ProfilePostSchema(Schema):
    id_user = fields.Int(required=True)
    identnumber = fields.Str(required=True)
    id_identtype = fields.Int(required=True)
    name = fields.Str(required=True)
    last_name_1 = fields.Str(required=True)
    last_name_2 = fields.Str()
    email = fields.Email(required=True)
    phone = fields.Str(required=True)

class ProfilePutSchema(Schema):
    id_user = fields.Int()
    identnumber = fields.Str()
    id_identtype = fields.Int()
    name = fields.Str()
    user_name = fields.Str()
    last_name_1 = fields.Str()
    last_name_2 = fields.Str()
    email = fields.Email()
    phone = fields.Str()