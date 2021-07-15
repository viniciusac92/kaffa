from sqlalchemy import Column, Integer, ForeignKey, String
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class OperatorCashierModel(db.Model):
    id: int
    id_operator: int
    id_cashier: int

    __tablename__ = "operator_cashier"

    id = Column(Integer, primary_key=True)
    id_operator = Column(Integer, ForeignKey("operators.id"), nullable=False)
    id_cashier = Column(Integer, ForeignKey("cashiers.id"), nullable=False)
