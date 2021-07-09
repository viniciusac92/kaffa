from dataclasses import dataclass
from sqlalchemy import Column, Integer

from app.configs.database import db

class MesaModel(db.Model):
    id: int
    numero: int

    __tablename__ = "mesas"

    id = Column(Integer, primary_key=True)
    numero = Column(Integer, nullable=False)