from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import relationship, backref
from app.configs.database import db
from dataclasses import dataclass

@dataclass
class CaixaModel(db.Model):
    id: int
    valor_inicial: float
    saldo: float
    lista_contas: list

    __tablename__ = "caixas"

    id = Column(Integer, primary_key=True)
    valor_inicial = Column(Float, default=0.0)
    saldo = Column(Float, default=0.0)

    lista_contas = relationship("ContaModel", backref=backref("caixa", uselist=False))

    def update_balance_all_bills(self):
        accum = 0
        
        for conta in self.lista_contas:
            accum = accum + conta.update_value()
        
        self.saldo = round(accum, 2)

        return self.saldo

    def remove_from_balance(self, value):
        self.saldo = self.saldo - value



