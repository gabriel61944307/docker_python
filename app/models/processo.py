# pylint: disable=C0114, C0115
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from ..db import Base

class Processo(Base):
    __tablename__ = 'processos'

    nro_processo = Column(Integer, primary_key=True, index=True)
    polo_ativo = Column(String, nullable=False)
    polo_passivo = Column(String, nullable=False)

class ProcessoSchema(BaseModel):
    nro_processo: int
    polo_ativo: str
    polo_passivo: str
