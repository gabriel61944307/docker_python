# pylint: disable=C0114, C0115, C0116
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.repositories.processo_operations import criar, listar
from app.models.processo import ProcessoCreate, ProcessoRead

router = APIRouter(prefix="/processos", tags=["clientes"])

@router.post("/", response_model=ProcessoRead)
def add_cliente(cliente: ProcessoCreate, db: Session = Depends(get_db)):
    return criar(db, cliente)

@router.get("/", response_model=list[ProcessoRead])
def listar_clientes(db: Session = Depends(get_db)):
    return listar(db)
