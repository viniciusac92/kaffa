from sqlalchemy import Column, Date, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship, backref
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
    lista_produtos: list

    __tablename__ = "contas"

    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    id_caixa = Column(Integer, ForeignKey("caixas.id"), nullable=False)
    id_garcom = Column(Integer, ForeignKey("garcons.id"), nullable=False)
    id_mesa = Column(Integer, ForeignKey("mesas.id"), nullable=False)
    id_forma_pagamento = Column(Integer, ForeignKey("forma_pagamento.id"), nullable=False)

    lista_produtos = relationship("ProdutoModel", secondary="conta_produto", backref=backref("contas_list"))
    
    def update_value(self):
        return sum([
            produto.preco
            for produto in self.lista_produtos
        ])
        