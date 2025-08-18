# pylint: disable=C0114, C0115, C0116
from sqlalchemy.orm import Session
from app.models.cliente import Cliente, ClienteCreate, ClienteRead

# Criar cliente
def criar(db: Session, cliente_data: ClienteCreate):
    cliente = Cliente(**cliente_data.model_dump())
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

# Buscar todos os clientes
def listar(db: Session):
    clientes = db.query(Cliente).all()
    return [ClienteRead.model_validate(c, from_attributes=True) for c in clientes]
