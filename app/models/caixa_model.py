from sqlalchemy import Column, Integer, Float
from app.configs.database import db
from dataclasses import dataclass

@dataclass
class CaixaModel(db.Model):
    id: int
    valor_inicial: float
    saldo: float

    __tablename__ = "caixas"

    id = Column(Integer, primary_key=True)
    valor_inicial = Column(Float, default=0.0)
    saldo = Column(Float)

    #método para consolidar contas no caixa

    #método para retirada de caixa

    


