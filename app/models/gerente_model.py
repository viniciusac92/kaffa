from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class GerenteModel(db.Model):
    id: int
    nome: str
    id_usuario: int

    __tablename__ = "gerentes"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False, unique=True)

    usuario = relationship('UserModel', backref=backref('gerente', uselist=False))
