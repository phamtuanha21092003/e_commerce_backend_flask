from db import db
from sqlalchemy import JSON


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    description = db.Column(db.String(1000), nullable=False)
    images = db.Column(JSON, nullable=False)
    brand = db.Column(db.String(100), nullable=False, index=True)
    sold = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False, index=True)
    category = db.relationship("Category", back_populates="products")
    variants = db.relationship("Variant", back_populates="product", cascade="all, delete-orphan")
