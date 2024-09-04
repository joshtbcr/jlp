from .. import models,schemas, auth
from app.crud import cuentaCRUD
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix='/cuentas',
    tags=['Cuentas']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Cuenta)
def create_cuenta(cuentaACrear: schemas.CuentaCreate, db: Session = Depends(get_db)):
    
    ## Permiso 0 = admin
    ## Permiso 1 = normal
    raise HTTPException (status_code=status.HTTP_306_RESERVED,
                        detail=f"Cuenta se crea con la creacion de un prestamo.")
    if usuarioExistente is not None:
        print(f"Usuario ya existe: {usuarioExistente}")

    cuentaACrear = cuentaCRUD.create_cuenta(db, usuario)
    print(f"Usuario creado: {nuevo_usuario}")

    return nuevo_usuario


@router.get("/",response_model=List[schemas.Cuenta])
def get_cuentas(db: Session = Depends(get_db),
                id_usuario: Optional[str] = ""):
    cuentas_existentes = cuentaCRUD.get_cuentas(db, id_usuario)

    if not cuentas_existentes:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No hay cuentas existentes.")
    
    return cuentas_existentes