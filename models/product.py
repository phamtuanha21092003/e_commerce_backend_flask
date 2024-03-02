from db import db
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped
from typing import List


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    description = db.Column(db.String(1000), nullable=False)
    images = db.Column(JSON, nullable=False)
    sold_quantity = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )
    brand_id = db.Column(
        db.Integer, db.ForeignKey("brands.id"), nullable=False, index=True
    )
    brand = db.relationship("Brand", back_populates="products")
    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.id"), nullable=False, index=True
    )
    category = db.relationship("Category", back_populates="products")
    product_variant_options: Mapped[List["ProductVariantOption"]] = db.relationship(
        back_populates="product"
    )
    product_combinations: Mapped[List["ProductCombination"]] = db.relationship(
        back_populates="product"
    )
