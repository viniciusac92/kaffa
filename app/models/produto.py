from sqlalchemy import Column, String, Integer
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref

from app.configs.database import db

@dataclass
class ProdutoModel(db.Model):
    id: int
    descricao: str
    preco: float

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    descricao = Column(String(200), nullable=False)

    estoque = relationship("EstoqueProdutoModel", backref=backref("lista_produtos"), uselist=False)