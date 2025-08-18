# pylint: disable=C0114, C0115, C0116
from contextlib import contextmanager
from sqlalchemy.exc import SQLAlchemyError
from app.db import SessionLocal
from app.models.processo import Processo, ProcessoSchema

@contextmanager
def _db_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()

# Criar cliente
def criar(polo_ativo: str, polo_passivo: str):
    with _db_session() as session:
        processo = Processo(polo_ativo=polo_ativo, polo_passivo=polo_passivo)
        session.add(processo)
        session.flush()
        return ProcessoSchema.model_validate(processo, from_attributes=True)

# Buscar todos os clientes
def listar():
    with _db_session() as session:
        processos = session.query(Processo).all()
        return [ProcessoSchema.model_validate(p, from_attributes=True) for p in processos]
