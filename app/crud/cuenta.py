from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime


def create_cuenta(db: Session, cuenta: schemas.CuentaCreate, usuario_id: int):
    db_prestamo = models.Prestamo(**cuenta.prestamo.dict())
    db.add(db_prestamo)
    db.commit()
    db_cuenta = models.Cuenta(**cuenta.dict(), usuario_id=usuario_id, prestamo_id=db_prestamo.id)
    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta
