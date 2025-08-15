# pylint: disable=C0114, C0115, C0116
from contextlib import contextmanager
from sqlalchemy.exc import SQLAlchemyError
from app.db import SessionLocal
from app.models.cliente import Cliente

@contextmanager
def __db_session():
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
def criar_cliente(nome: str, email: str):
    with __db_session() as session:
        cliente = Cliente(nome=nome, email=email)
        session.add(cliente)
        session.flush()
        return{
            "id": cliente.id,
            "nome": cliente.nome,
            "email": cliente.email
        }

# Buscar todos os clientes
def listar_clientes():
    clientes = []
    with __db_session() as session:
        clientes_object = session.query(Cliente).all()
        for c in clientes_object:
            clientes.append({
                "id": c.id,
                "nome": c.nome,
                "email": c.email
            })
    return clientes
