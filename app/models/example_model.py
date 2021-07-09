# from sqlalchemy.orm import backref
# from app import db
# from sqlalchemy import Column, Integer, String, ForeignKey

# class CapitaisModel(db.Model):
#     __tablename__ = "capitais"

#     id = Column(Integer, primary_key=True)
#     nome = Column(String(50), nullable=False, unique=True)
#     bairros = Column(Integer)
#     populacao = Column(Integer)

#     estado = db.relationship(
#         "EstadosModel", backref=db.backref("capital",uselist=False)
#     )

#     estado_id = Column(
#         Integer, ForeignKey("estados.id"), nullable=False, unique=True
#     )

# test model
