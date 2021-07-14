from sqlalchemy import Column, Integer, ForeignKey, String
from app.configs.database import db
from dataclasses import dataclass

@dataclass
class OperadorCaixaModel(db.Model):
    id: int
    id_operador: int
    id_caixa: int

    __tablename__ = "operador_caixa"

    id = Column(Integer, primary_key=True)
    id_operador = Column(Integer, ForeignKey("operadores.id"), nullable=False)
    id_caixa = Column(Integer, ForeignKey("caixas.id"), nullable=False)
    