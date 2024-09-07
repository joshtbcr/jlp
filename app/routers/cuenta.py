
from .. import models,schemas, auth
from app.crud import cuentaCRUD
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional
import io

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
    print(f"==>> cuentas_existentes: {cuentas_existentes}")

    if not cuentas_existentes:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No hay cuentas existentes.")
    
    return cuentas_existentes

@router.get("/generate-excel/")
def get_cuentas(db: Session = Depends(get_db),
                id_usuario: str = ""):
    if id_usuario =="":
            raise HTTPException (status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Necesita ID de usuario.")
    
    # cuentas_existentes = cuentaCRUD.get_cuentas(db, id_usuario)[0]
    # print(f"==>> cuentas_existentes: {cuentas_existentes}")


    # if not cuentas_existentes:
    #     raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"No hay cuentas existentes.")

    output = io.BytesIO()
    output = cuentaCRUD.get_Excel(db, output, id_usuario)

    headers = {
        'Content-Disposition': 'attachment; filename="estado_de_cuenta.xlsx"'
    }
    
    return StreamingResponse(output, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', headers=headers)



