from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float, ForeignKey


class ProductCombination(db.Model):
    __tablename__ = "product_combinations"

    __table_args__ = (
        db.CheckConstraint(
            "origin_price > sale_price", name="check_origin_price_sale_price"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    combination_name: Mapped[str] = mapped_column(String(255), index=True)
    warehouse_quantity: Mapped[int] = mapped_column(Integer)
    origin_price: Mapped[float] = mapped_column(Float)
    sale_price: Mapped[float] = mapped_column(Float)
    image: Mapped[str] = mapped_column(String(255))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), index=True)
    product: Mapped["Product"] = db.relationship(back_populates="product_combinations")
