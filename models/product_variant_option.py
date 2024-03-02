from db import db
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from typing import List


class ProductVariantOption(db.Model):
    __tablename__ = "product_variant_options"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), index=True)
    product: Mapped["Product"] = db.relationship(
        back_populates="product_variant_options"
    )
    product_variant_values: Mapped[List["ProductVariantOptionValue"]] = db.relationship(
        back_populates="product_variant_name"
    )
