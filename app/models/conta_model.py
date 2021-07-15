from sqlalchemy import Column, Date, Integer, Boolean, and_
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass
from datetime import date

import ipdb

from .conta_produto import ContaProdutoModel

from app.configs.database import db

@dataclass
class ContaModel(db.Model):
    id: int
    data: date
    id_caixa: int
    id_garcom: int
    id_mesa: int
    id_forma_pagamento: int
    is_finished: bool
    lista_produtos: list

    __tablename__ = "contas"

    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    id_caixa = Column(Integer, ForeignKey("caixas.id"), nullable=False)
    id_garcom = Column(Integer, ForeignKey("garcons.id"), nullable=False)
    id_mesa = Column(Integer, ForeignKey("mesas.id"), nullable=False)
    id_forma_pagamento = Column(Integer, ForeignKey("forma_pagamento.id"), nullable=False)
    is_finished = Column(Boolean, default=False)

    lista_produtos = relationship("ProdutoModel", secondary="conta_produto", backref=backref("contas_list"))
    
    def get_value(self):
        bill_value = 0

        for produto in self.lista_produtos:
            conta_produto: ContaProdutoModel = ContaProdutoModel.query.filter(and_(ContaProdutoModel.id_produto == produto.id, ContaProdutoModel.id_conta == self.id)).first()
            bill_value = bill_value + (produto.preco * conta_produto.quantity)
        
        return bill_value        

    def close_bill(self):
        bill_value = 0

        for produto in self.lista_produtos:
            conta_produto: ContaProdutoModel = ContaProdutoModel.query.filter(and_(ContaProdutoModel.id_produto == produto.id, ContaProdutoModel.id_conta == self.id)).first()
            produto.remove_from_stock(conta_produto.quantity)
            bill_value = bill_value + (produto.preco * conta_produto.quantity)

        self.is_finished = True
        return bill_value      

