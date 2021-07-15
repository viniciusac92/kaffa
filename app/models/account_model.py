from sqlalchemy import Column, Date, Integer, and_
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass
from datetime import date

import ipdb

from .account_product import AccountProductModel

from app.configs.database import db


@dataclass
class AccountModel(db.Model):
    id: int
    date: date
    id_cashier: int
    id_waiter: int
    id_table: int
    id_payment_method: int
    product_list: list

    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    id_cashier = Column(Integer, ForeignKey("cashiers.id"), nullable=False)
    id_waiter = Column(Integer, ForeignKey("waiters.id"), nullable=False)
    id_table = Column(Integer, ForeignKey("tables.id"), nullable=False)
    id_payment_method = Column(Integer, ForeignKey(
        "payment_method.id"), nullable=False)

    product_list = relationship(
        "ProductModel", secondary="account_product", backref=backref("account_list"))

    def update_value(self):
        bill_value = 0

        for product in self.product_list:
            account_product: AccountProductModel = AccountProductModel.query.filter(and_(
                AccountProductModel.id_product == product.id, AccountProductModel.id_account == self.id)).first()
            bill_value = bill_value + \
                (product.price * account_product.quantity)

        return bill_value
