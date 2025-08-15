from sqlalchemy import Column, Integer, String
from ..db import Base
# pylint: disable=C0114, C0115

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
