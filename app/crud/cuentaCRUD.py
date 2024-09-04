from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime


def create_cuenta(db: Session, prestamo: schemas.Prestamo, usuario_id: int):
    
    cuenta = schemas.CuentaCreate(
        prestamo_id=prestamo.id,
        moneda=prestamo.moneda,
        balance=prestamo.monto
    )
    db_cuenta = models.Cuenta(**cuenta.dict())

    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta


def get_cuentas(db: Session, usuario_id: int = 1):
    # return db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).all()
    return db.query(models.Cuenta).all()

