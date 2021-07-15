from sqlalchemy import Column, String, Integer, ForeignKey
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class AccountProductModel(db.Model):
    id: int
    id_account: int
    id_product: int
    quantity: int

    __tablename__ = "account_product"

    id = Column(Integer, primary_key=True)
    id_account = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    id_product = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, default=1)

    def update_quantity(self, qt):
        self.quantity = qt
