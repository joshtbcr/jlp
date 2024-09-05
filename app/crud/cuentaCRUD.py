from typing import List
from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime


def create_cuenta(db: Session, prestamo: schemas.Prestamo, usuario_id: str):
    
    id_usuario = str(db.query(models.Usuario).filter(models.Usuario.id_usuario == str(usuario_id)).first().id)
    print(f"==>> id_usuario: {id_usuario}")

    
    cuenta = schemas.CuentaCreate(
        prestamo_id=prestamo.id,
        moneda=prestamo.moneda,
        balance=prestamo.monto,
        usuario_id=id_usuario
    )
    db_cuenta = models.Cuenta(**cuenta.dict())

    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta


def get_cuentas(db: Session, id_usuario):
    #TODO
    permiso_usuario = 0
    
    print(f"==>> id_usuario: {id_usuario}")
    if id_usuario == "":
        if permiso_usuario == 0:
            cuentas_existentes = db.query(models.Cuenta).all()
            return cuentas_existentes   
        elif permiso_usuario > 0:
            cuentas_existentes = List[schemas.Cuenta]
            return cuentas_existentes
    else:   
        print(f"==>>Obteniendo todas las cuestas del usuario: {id_usuario}")
        cuentas_existentes = db.query(models.Cuenta).filter(models.Cuenta.usuario_id == id_usuario).all()
        return cuentas_existentes   
    
    return db.query(models.Cuenta).all()

