from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer


@dataclass
class FornecedorProdutoModel(db.Model): 
    id: int
    id_produto: int
    id_fornecedor: int

    __tablename__ = 'fornecedor_produto'

    id = Column(Integer, primary_key=True)

    id_produto = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    id_fornecedor = Column(Integer, ForeignKey("fornecedor.id"), nullable=False)