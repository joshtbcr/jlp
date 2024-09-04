from sqlalchemy.orm import Session
from app import models, schemas
from . import cuentaCRUD, usuarioCRUD
from datetime import datetime


def create_prestamo(db: Session, prestamo: schemas.PrestamoCreate):

    db_prestamo = models.Prestamo(**prestamo.dict(exclude={'usuario_id'}))
    db.add(db_prestamo)
    db.commit()
    
    db.refresh(db_prestamo)

    #crear cuenta
    nuevaCuenta = cuentaCRUD.create_cuenta(db, db_prestamo, prestamo.usuario_id)
    
    return db_prestamo


def get_prestamo(db: Session, usuario_id: int = 1):
    # return db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).all()
    return db.query(models.Prestamo).all()

