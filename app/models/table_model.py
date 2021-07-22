from dataclasses import dataclass
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship, backref


from app.configs.database import db


@dataclass
class TableModel(db.Model):
    id: int
    number: int
    account_list: list

    __tablename__ = "tables"

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False, unique=True)

    account_list = relationship("AccountModel", backref=backref("table"))
