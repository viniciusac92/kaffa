from sqlalchemy import Column, String, Integer
from app.configs.database import db
from dataclasses import dataclass
from werkzeug.security import check_password_hash, generate_password_hash

@dataclass
class GarcomModel(db.Model):
    id: int
    nome: str
    password_hash: str

    __tablename__ = "garcons"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    password_hash = Column(String)

    @property
    def password(self):
        raise "O password não pode ser acessado!"

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)