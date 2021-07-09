from dataclasses import dataclass
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship, backref


from app.configs.database import db

@dataclass
class MesaModel(db.Model):
    id: int
    numero: int

    __tablename__ = "mesas"

    id = Column(Integer, primary_key=True)
    numero = Column(Integer, nullable=False)

    lista_contas = relationship("ContaModel", backref=backref("mesa", uselist=False))
