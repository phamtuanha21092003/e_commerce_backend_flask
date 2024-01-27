from marshmallow import Schema, fields, validate

class SignInSchema(Schema):
    email = fields.Email(required=True, validate=validate.Email(), allow_none=False)
    password = fields.String(required=True, allow_none=False)