from sqlalchemy import Column, Integer, String
from ..db import Base
# pylint: disable=C0114, C0115

class Cliente(Base):
    __tablename__ = 'processos_3r'

    nro_processo = Column(Integer, primary_key=True, index=True)
    polo_ativo = Column(String, nullable=False)
    polo_passivo = Column(String, nullable=False)
