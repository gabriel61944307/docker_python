# pylint: disable=C0114, C0115
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from ..db import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)

class ClienteSchema(BaseModel):
    id: int
    nome: str
    email: str
