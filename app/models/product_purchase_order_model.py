from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import backref, relationship


@dataclass
class ProductPurchaseOrderModel(db.Model):
    id: int
    id_order: int
    id_product: int

    __tablename__ = 'product_purchase_order'

    id = Column(Integer, primary_key=True)

    id_order = Column(Integer, ForeignKey("purchase_order.id"), nullable=False)
    id_product = Column(Integer, ForeignKey("products.id"), nullable=False)
