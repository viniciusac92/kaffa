from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class OperadorModel(db.Model):
    id: int
    nome: str
    cpf: str
    lista_caixas: list

    __tablename__ = "operadores"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False, unique=True)

    lista_caixas = relationship(
        "CaixaModel", backref=backref("operadores_list"), secondary="operador_caixa"
    )

    usuario = relationship('UserModel', backref=backref('operador', uselist=False))
