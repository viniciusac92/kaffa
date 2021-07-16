from dataclasses import dataclass
from datetime import date

from app.configs.database import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Boolean, Float, and_
from sqlalchemy.orm import backref, relationship

from .product_purchase_order_model import ProductPurchaseOrderModel
@dataclass
class PurchaseOrderModel(db.Model):
    id: int
    id_manager: int
    id_provider: int
    date: date
    is_finished: bool
    total_value: float
    products_list: list

    __tablename__ = 'purchase_order'

    id = Column(Integer, primary_key=True)

    id_manager = Column(Integer, ForeignKey("managers.id"), nullable=False)    
    id_provider = Column(Integer, ForeignKey(
        "provider.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    is_finished = Column(Boolean, default=False)
    total_value = Column(Float, default=0.0)
    
    products_list = relationship(
        'ProductModel', backref=backref('purchase_order_list'), secondary='product_purchase_order'
    )

    # def get_value(self):
    #     order_value = 0

    #     for product in self.products_list:
    #         product_purchase_order: ProductPurchaseOrderModel = ProductPurchaseOrderModel.query.filter(and_(
    #             ProductPurchaseOrderModel.id_product == product.id, ProductPurchaseOrderModel.id_account == self.id)).first()
    #         order_value = order_value + \
    #             (product.price * product_purchase_order.quantity)

    #     return order_value

    def close_order(self):
        order_value = 0

        if not self.is_finished:
            for product in self.products_list:
                product_purchase_order: ProductPurchaseOrderModel = ProductPurchaseOrderModel.query.filter(and_(
                    ProductPurchaseOrderModel.id_product == product.id, ProductPurchaseOrderModel.id_order == self.id)).first()
                product.add_to_stock(product_purchase_order.quantity)
                order_value = order_value + \
                    (product.price * product_purchase_order.quantity)
            
            self.is_finished = True
            self.total_value = order_value
