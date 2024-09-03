from .. import models,schemas, auth
from app.crud import usuarioCRUD
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix='/usuarios',
    tags=['Usuarios']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    

    nuevo_usuario = usuarioCRUD.create_usuario(db, usuario)
    print("Usuario creado")

    return nuevo_usuario


@router.get("/{id}",response_model=schemas.Usuario)
def get_usuario(id:int, db: Session = Depends(get_db)):
    usuario = db.query(models.usuario).filter(models.usuario.id ==id).first()

    if not usuario:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"usuario with id {id} was not found.")
    
    return usuario