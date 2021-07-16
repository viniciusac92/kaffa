from dataclasses import dataclass
from datetime import date

from app.configs.database import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Boolean
from sqlalchemy.orm import backref, relationship

from .product_purchase_order_model import ProductPurchaseOrderModel
@dataclass
class PurchaseOrderModel(db.Model):
    id: int
    id_manager: int
    id_provider: int
    date: date
    is_finished: bool
    products_list: list

    __tablename__ = 'purchase_order'

    id = Column(Integer, primary_key=True)

    id_manager = Column(Integer, ForeignKey("managers.id"), nullable=False)    
    id_provider = Column(Integer, ForeignKey(
        "provider.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    is_finished = Column(Boolean, default=False)
    
    products_list = relationship(
        'ProductModel', backref=backref('purchase_order_list'), secondary='product_purchase_order'
    )

    def get_value(self):
        order_value = 0

        for product in self.products_list:
            product_purchase_order: ProductPurchaseOrderModel = ProductPurchaseOrderModel.query.filter(and_(
                ProductPurchaseOrderModel.id_product == product.id, ProductPurchaseOrderModel.id_account == self.id)).first()
            order_value = order_value + \
                (product.price * account_product.quantity)

        return order_value

    def close_order(self):
        order_value = 0

        for product in self.products_list:
            account_product: AccountProductModel = AccountProductModel.query.filter(and_(
                AccountProductModel.id_product == product.id, AccountProductModel.id_account == self.id)).first()
            product.remove_from_stock(account_product.quantity)
            bill_value = bill_value + \
                (product.price * account_product.quantity)
        
        self.is_finished = True
        return bill_value
