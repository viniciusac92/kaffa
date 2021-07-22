from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship
from werkzeug.security import check_password_hash, generate_password_hash


@dataclass
class UserModel(db.Model):
    id: int
    username: str
    type: int
    # password_hash: str

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    username = Column(String(50), nullable=False, unique=True)
    type = Column(Integer, nullable=False)
    password_hash = Column(String, nullable=False)

    @property
    def password(self):
        raise "Password not accessible"

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
