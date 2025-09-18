from . import auth
from .. import models,schemas
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
    
    ## Permiso 0 = admin
    ## Permiso 1 = normal
    usuarioExistente = usuarioCRUD.get_usuario(db, usuario.cedula)
    if usuarioExistente is not None:
        print(f"Usuario ya existe: {usuarioExistente}")
        raise HTTPException (status_code=status.HTTP_409_CONFLICT,
                            detail=f"Usuario con este id ya existe.")

    nuevo_usuario = usuarioCRUD.create_usuario(db, usuario)
    print(f"Usuario creado: {nuevo_usuario}")

    return nuevo_usuario



@router.get("/")
def get_usuario(cedula:str, db: Session = Depends(get_db)):
    usuarioExistente = usuarioCRUD.get_usuario(db, cedula)

    if not usuarioExistente:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Usuario con cedula {cedula} no fue encontrado.")
    
    return usuarioExistente

@router.get("/{cedula}",response_model=schemas.Usuario)
def get_usuario(cedula:str | None = None, db: Session = Depends(get_db)):
    usuario = usuarioCRUD.get_usuario(db, cedula)

    if not usuario:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Usuario con cedula {cedula} no fue encontrado.")
    
    return usuario
