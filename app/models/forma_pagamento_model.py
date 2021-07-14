from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from app.configs.database import db

@dataclass
class FormaPagamentoModel(db.Model):
    id: int
    nome: str
    descricao: str
    lista_contas: list

    __tablename__ = "forma_pagamento"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)
    descricao = Column(String(150), nullable=True)

    lista_contas = relationship("ContaModel", backref=backref("forma_pagamento"))
