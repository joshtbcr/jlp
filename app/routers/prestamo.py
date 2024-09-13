from typing import List

from . import auth
from .. import models,schemas
from app.crud import prestamoCRUD, usuarioCRUD
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix='/prestamos',
    tags=['Prestamo']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Prestamo)
def create_prestamo(prestamoACrear: schemas.PrestamoCreate, db: Session = Depends(get_db)):

    
    # usuarioExistente = usuarioCRUD.get_usuario(db, prestamoACrear.usuario_id)
    # if usuarioExistente is None:
    #     print(f"Usuario con id: '{usuarioExistente}' no existe.")
    #     raise HTTPException (status_code=status.HTTP_400_BAD_REQUEST,
    #                         detail=f"Usuario con este id no existe.")


    nuevo_prestamo = prestamoCRUD.create_prestamo(db, prestamoACrear)
    print(f"Prestamo creado: {nuevo_prestamo}")

    return nuevo_prestamo


@router.get("/",response_model=List[schemas.Prestamo])
def get_prestamos(db: Session = Depends(get_db)):
    
    prestamos = prestamoCRUD.get_prestamo(db,usuario_cedula=1)
    # print(f"==>> prestamos: {prestamos}")
    
    if not prestamos:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Prestamos no disponibles.")
    
    return prestamos
