# from sqlalchemy import Column, Integer
# from dataclasses import dataclass
# from sqlalchemy.sql.schema import ForeignKey

# from app.configs.database import db


# @dataclass
# class StockProductModel(db.Model):
#     id: int
#     id_product: int
#     quantity: int

#     __tablename__ = "stock_product"

#     id = Column(Integer, primary_key=True)
#     id_product = Column(Integer, ForeignKey("products.id"),
#                         nullable=False, unique=True)
#     quantity = Column(Integer, nullable=False)
