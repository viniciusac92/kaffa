from dataclasses import dataclass
from sqlalchemy import Column, Integer, String

from app.configs.database import db

class FormaPagamentoModel(db.Model):
    id: int
    descricao: str

    __tablename__ = "forma_pagamento"

    id = Column(Integer, primary_key=True)
    descricao = Column(String(50), nullable=False)