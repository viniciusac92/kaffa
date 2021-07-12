from sqlalchemy import Column, String, Integer, DECIMAL
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref

from app.configs.database import db

@dataclass
class ProdutoModel(db.Model):
    id: int
    descricao: str

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)
    descricao = Column(String(200), nullable=False)
