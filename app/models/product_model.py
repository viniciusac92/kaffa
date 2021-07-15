from decimal import Decimal
from sqlalchemy import Column, String, Integer, Float
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.sqltypes import Numeric

from app.configs.database import db


@dataclass
class ProductModel(db.Model):
    id: int
    name: str
    description: str
    price: float

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(200), nullable=True)
    price = Column(Float, nullable=False)
