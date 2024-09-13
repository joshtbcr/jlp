from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

from app.routers import auth


def get_usuario(db: Session, cedula: str):
    if cedula:
        return db.query(models.Usuario).filter(models.Usuario.cedula == cedula).first()
    return db.query(models.Usuario).all()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):

    usuario.contrasena = auth.hash(usuario.contrasena)
    nuevo_usuario = models.Usuario(**usuario.dict())
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario