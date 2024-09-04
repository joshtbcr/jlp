from sqlalchemy.orm import Session
from app import models, schemas, auth
from datetime import datetime


def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()



def create_usuario(db: Session, usuario: schemas.UsuarioCreate):

    usuario.contrasena = auth.hash(usuario.contrasena)
    nuevo_usuario = models.Usuario(**usuario.dict())
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario