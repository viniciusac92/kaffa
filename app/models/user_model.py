from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref
from app.configs.database import db
from dataclasses import dataclass
from werkzeug.security import check_password_hash, generate_password_hash

@dataclass
class UserModel(db.Model):
    id: int
    username: str
    tipo: int
    password_hash: str

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    tipo = Column(Integer, nullable=False)
    password_hash = Column(String, nullable=False)

    @property
    def password(self):
        raise "O password não pode ser acessado!"

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)