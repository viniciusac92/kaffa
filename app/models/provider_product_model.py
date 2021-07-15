from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer


@dataclass
class ProviderProductModel(db.Model):
    id: int
    id_product: int
    id_provider: int

    __tablename__ = 'provider_product'

    id = Column(Integer, primary_key=True)

    id_product = Column(Integer, ForeignKey("products.id"), nullable=False)
    id_provider = Column(Integer, ForeignKey(
        "provider.id"), nullable=False)
