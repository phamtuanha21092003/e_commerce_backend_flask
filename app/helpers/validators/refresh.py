from marshmallow import Schema, fields


class RefreshSchema(Schema):
    token = fields.Str(required=True)
