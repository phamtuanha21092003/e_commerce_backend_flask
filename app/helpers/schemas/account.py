from schemas import ma
from models import Account
from models.account import AccountRole
from marshmallow import validate, fields


class AccountSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Account

    id = ma.auto_field()
    username = ma.auto_field()
    password = ma.auto_field()
    email = ma.auto_field(validate=validate.Email())
    role = fields.Method("_get_role", "_load_role")

    def _get_role(self, obj):
        return obj.role.name if obj.role else None

    def _load_role(self, role_name):
        return AccountRole[role_name] if role_name else None
