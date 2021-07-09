from sqlalchemy import Column, Date, Integer
from sqlalchemy.sql.schema import ForeignKey
from dataclasses import dataclass
from datetime import date

from app.configs.database import db

@dataclass
class ContaModel(db.Model):
    id: int
    data: date
    id_caixa: int
    id_garcom: int
    id_mesa: int
    id_forma_pagamento: int

    __tablename__ = "contas"

    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    id_caixa = Column(Integer, ForeignKey("caixas.id"), nullable=False)
    id_garcom = Column(Integer, ForeignKey("garcons.id"), nullable=False)
    id_mesa = Column(Integer, ForeignKey("mesas.id"), nullable=False)
    id_forma_pagamento = Column(Integer, ForeignKey("forma_pagamento.id"))
