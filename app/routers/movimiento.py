from typing import List

from . import auth
from .. import models,schemas
from app.crud import movimientoCRUD
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix='/movimientos',
    tags=['Movimientos']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Movimiento)
def create_movimiento(movimientoACrear: schemas.MovimientoCreate, db: Session = Depends(get_db)):
    
    nuevo_movimiento = movimientoCRUD.create_movimiento(db, movimientoACrear)
    print(f"Movimiento creado: {nuevo_movimiento}")

    return nuevo_movimiento


@router.get("/",response_model=List[schemas.Movimiento])
def get_movimiento(db: Session = Depends(get_db)):
    
    movimientos = movimientoCRUD.get_movimientos(db)

    if not movimientos:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Movimientos no disponibles.")
    
    return movimientos
