from db import db
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column


class ProductVariantOptionValue(db.Model):
    __tablename__ = "product_variant_option_values"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    value: Mapped[str] = mapped_column(String(50), index=True)
    product_variant_name_id: Mapped[int] = mapped_column(
        ForeignKey("product_variant_options.id")
    )
    product_variant_name: Mapped["ProductVariantOption"] = db.relationship(
        back_populates="product_variant_values"
    )
