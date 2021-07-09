from sqlalchemy import Column, Integer
from dataclasses import dataclass
from sqlalchemy.sql.schema import ForeignKey

from app.configs.database import db

@dataclass
class EstoqueProdutoModel(db.Model):
    id: int
    id_produto: int
    quantidade: int

    __tablename__ = "estoque_produto"

    id = Column(Integer, primary_key=True)
    id_produto = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)

    # método pra calcular quantidade?