from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref
from app.configs.database import db
from dataclasses import dataclass
from werkzeug.security import check_password_hash, generate_password_hash

@dataclass
class OperadorModel(db.Model):
    id: int
    nome: str
    password_hash: str

    __tablename__ = "operadores"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    password_hash = Column(String)

    lista_caixas = relationship("CaixaModel", backref=backref("lista_operadores"), secondary="operadores_caixa")

    @property
    def password(self):
        raise "O password não pode ser acessado!"

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)