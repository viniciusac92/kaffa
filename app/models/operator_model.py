from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class OperatorModel(db.Model):
    id: int
    name: str
    cpf: str
    cashier_list: list

    __tablename__ = "operators"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    id_user = Column(Integer, ForeignKey("user.id"),
                     nullable=False, unique=True)

    cashier_list = relationship("CashierModel", backref=backref(
        "operators_list"), secondary="operator_cashier")
