from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref

from app.configs.database import db
from dataclasses import dataclass
from werkzeug.security import check_password_hash, generate_password_hash

@dataclass
class GerenteModel(db.Model):
    id: int
    nome: str

    __tablename__ = "gerentes"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)