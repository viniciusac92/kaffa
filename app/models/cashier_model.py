from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Float, Integer
from sqlalchemy.orm import backref, relationship


@dataclass
class CashierModel(db.Model):
    id: int
    initial_value: float
    balance: float

    __tablename__ = "cashiers"

    id = Column(Integer, primary_key=True)
    initial_value = Column(Float, default=0.0)
    balance = Column(Float, default=0.0)

    account_list = relationship(
        "AccountModel", backref=backref("cashier", uselist=False)
    )

    def update_balance_all_bills(self):
        accum = 0

        for account in self.account_list:
            accum = accum + account.update_value()

        self.balance = round(accum, 2)

        return self.balance

    def remove_from_balance(self, value):
        self.balance = self.balance - value
