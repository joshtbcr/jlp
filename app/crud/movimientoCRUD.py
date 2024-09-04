from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime


def create_movimiento(db: Session, cuenta: schemas.CuentaCreate, usuario_id: int):
    db_prestamo = models.Prestamo(**cuenta.prestamo.dict())
    db.add(db_prestamo)
    db.commit()
    
    db.refresh(db_prestamo)
    
    return db_prestamo


def get_movimientos(db: Session, usuario_id: int = 1):
    # return db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).all()
    return db.query(models.Movimiento).all()

