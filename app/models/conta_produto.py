from sqlalchemy import Column, String, Integer, ForeignKey
from app.configs.database import db
from dataclasses import dataclass

@dataclass
class ContaProdutoModel(db.Model):
    id: int
    id_conta: int
    id_produto: int
    quantity: int

    __tablename__ = "conta_produto"

    id = Column(Integer, primary_key=True)
    id_conta = Column(Integer, ForeignKey("contas.id"), nullable=False)
    id_produto = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    quantity = Column(Integer, default=1)

    def update_quantity(self, qt):
        self.quantity = qt

    