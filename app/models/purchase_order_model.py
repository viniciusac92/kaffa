from dataclasses import dataclass
from datetime import date

from app.configs.database import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import backref, relationship


@dataclass
class PurchaseOrderModel(db.Model):
    id: int
    id_fornecedor: int
    data: date
    lista_produtos: list

    __tablename__ = 'purchase_order'

    id = Column(Integer, primary_key=True)

    id_fornecedor = Column(Integer, ForeignKey(
        "fornecedor.id"), nullable=False)
    data = Column(DateTime, nullable=False)

    lista_produtos = relationship(
        'ProdutoModel', backref=backref('purchase_order_list'), secondary='produto_purchase_order'
    )
