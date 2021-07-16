from sqlalchemy import Column, String, Integer, ForeignKey
# from sqlalchemy.orm import relationship, backref

from app.configs.database import db
from dataclasses import dataclass
# from werkzeug.security import check_password_hash, generate_password_hash

@dataclass
class ManagerModel(db.Model):
    id: int
    name: str

    __tablename__ = "managers"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    id_user = Column(Integer, ForeignKey("user.id"), nullable=False, unique=True)
