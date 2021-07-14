from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import backref, relationship


@dataclass
class ProdutoOrdemDeCompraModel(db.Model):
    id: int
    id_ordem: int
    id_produto: int

    __tablename__ = 'produto_ordem_de_compra'

    id = Column(Integer, primary_key=True)

    id_ordem = Column(Integer, ForeignKey("ordem_de_compra.id"), nullable=False)
    id_produto = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    
