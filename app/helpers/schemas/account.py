from schemas import ma
from models import Account
from marshmallow import validate


class AccountSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Account

    id = ma.auto_field()
    username = ma.auto_field()
    password = ma.auto_field()
    email = ma.auto_field(validate=validate.Email())
    role = ma.auto_field()
