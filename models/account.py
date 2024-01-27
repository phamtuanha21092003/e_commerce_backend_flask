from db import db
import enum


class AccountRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"


class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(), unique=True, nullable=False, index=True)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False, index=True)
    role = db.Column(db.Enum(AccountRole), nullable=False, default=AccountRole.USER)