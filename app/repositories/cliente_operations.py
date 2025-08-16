# pylint: disable=C0114, C0115, C0116
from contextlib import contextmanager
from sqlalchemy.exc import SQLAlchemyError
from app.db import SessionLocal
from app.models.cliente import Cliente, ClienteSchema

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
def criar(nome: str, email: str):
    with _db_session() as session:
        cliente = Cliente(nome=nome, email=email)
        session.add(cliente)
        session.flush()
        return ClienteSchema.model_validate(cliente, from_attributes=True)

# Buscar todos os clientes
def listar():
    with _db_session() as session:
        clientes = session.query(Cliente).all()
        return [ClienteSchema.model_validate(c, from_attributes=True) for c in clientes]
