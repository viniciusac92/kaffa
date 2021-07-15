from dataclasses import dataclass
from datetime import date

from app.configs.database import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import backref, relationship


@dataclass
class PurchaseOrderModel(db.Model):
    id: int
    id_provider: int
    date: date

    __tablename__ = 'purchase_order'

    id = Column(Integer, primary_key=True)

    id_provider = Column(Integer, ForeignKey("provider.id"), nullable=False)
    date = Column(DateTime, nullable=False)

    products_list = relationship(
        'ProductModel',
        backref=backref('purchase_order_list'),
        secondary='product_purchase_order',
    )
