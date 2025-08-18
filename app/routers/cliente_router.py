# pylint: disable=C0114, C0115, C0116
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.repositories.cliente_operations import criar, listar
from app.models.cliente import ClienteCreate, ClienteRead

router = APIRouter(prefix="/clientes", tags=["clientes"])

@router.post("/", response_model=ClienteRead)
def add_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return criar(db, cliente)

@router.get("/", response_model=list[ClienteRead])
def listar_clientes(db: Session = Depends(get_db)):
    return listar(db)
