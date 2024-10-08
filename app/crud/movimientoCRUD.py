from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime


tipos_permitidos = [
    "Pago",
    "Interés"
]

def create_movimiento(db: Session, movimiento: schemas.Movimiento):
    if(movimiento.tipo in tipos_permitidos):
        db_movimiento = models.Movimiento(**movimiento.dict())
        db.add(db_movimiento)
        db.commit()
        
        db.refresh(db_movimiento)
        
        return db_movimiento


def get_movimientos(db: Session, usuario_id: int = 1):
    # return db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).all()

    movimientos = db.query(models.Movimiento).all()
    return movimientos

