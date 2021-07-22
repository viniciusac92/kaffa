from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class ProviderModel(db.Model):
    id: int
    trading_name: str
    cnpj: str
    phone: str
    product_list: list

    __tablename__ = 'provider'

    id = Column(Integer, primary_key=True)
    trading_name = Column(String(200), nullable=False)
    cnpj = Column(String(18), nullable=False, unique=True)
    phone = Column(String(12), nullable=False, unique=True)

    product_list = relationship(
        'ProductModel', backref=backref('provider_list'), secondary='provider_product'
    )
