# pylint: disable=C0114, C0115, C0116
from sqlalchemy.orm import Session
from app.models.processo import Processo, ProcessoCreate, ProcessoRead

# Criar cliente
def criar(db: Session, processo_data: ProcessoCreate):
    processo = Processo(**processo_data.model_dump())
    db.add(processo)
    db.commit()
    db.refresh(processo)
    return processo

# Buscar todos os clientes
def listar(db: Session):
    processos = db.query(Processo).all()
    return [ProcessoRead.model_validate(p, from_attributes=True) for p in processos]
