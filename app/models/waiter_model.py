from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.configs.database import db
from dataclasses import dataclass


@dataclass
class WaiterModel(db.Model):
    id: int
    name: str
    cpf: str
    account_list: list

    __tablename__ = "waiters"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    id_user = Column(Integer, ForeignKey("user.id"),
                     nullable=False, unique=True)

    account_list = relationship("AccountModel", backref=backref("waiter"))
