from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from app.configs.database import db


@dataclass
class PaymentMethodModel(db.Model):
    id: int
    name: str
    description: str
    account_list: list

    __tablename__ = "payment_method"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(150), nullable=True)

    account_list = relationship(
        "AccountModel", backref=backref("payment_method"))
