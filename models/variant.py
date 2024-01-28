from sqlalchemy import JSON
from db import db


class Variant(db.Model):
    __tablename__ = "variants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(100), nullable=False)
    default_price = db.Column(db.Float, nullable=False)
    sale_price = db.Column(db.Float, nullable=False)
    warehouse_quantity = db.Column(db.Integer, nullable=False)
    option = db.Column(JSON, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    product = db.relationship("Product", back_populates="variants", lazy=True)
