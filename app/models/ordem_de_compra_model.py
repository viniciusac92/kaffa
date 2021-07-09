from dataclasses import dataclass
from datetime import date

from app.configs.database import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import backref, relationship


@dataclass
class OrdemDeCompra(db.Model):
    id: int
    id_fornecedor: int
    data: date

    __tablename__ = 'ordem_de_compra'

    id = Column(Integer, primary_key=True)

    id_fornecedor = Column(Integer, ForeignKey("fornecedor.id"), nullable=False)
    data = Column(DateTime, nullable=False)

    fornecedor = relationship(
        'OrdemDeCompraModel', backref=backref('fornecedor'), uselist=False
    )
