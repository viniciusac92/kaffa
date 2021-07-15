from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class GarcomModel(db.Model):
    id: int
    nome: str
    cpf: str
    lista_contas: list

    __tablename__ = "garcons"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False, unique=True)

    lista_contas = relationship("ContaModel", backref=backref("garcom"))

    usuario = relationship('UserModel', backref=backref('garcom', uselist=False))
