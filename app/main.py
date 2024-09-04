from fastapi import FastAPI, Depends
from app import models, crud, auth, database
from .routers import usuario, cuenta, movimiento, prestamo
from app.database import engine
from app.dependencies import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Rutas de autenticación
app.include_router(auth.router)
app.include_router(usuario.router)
app.include_router(prestamo.router)
app.include_router(cuenta.router)
app.include_router(movimiento.router)

@app.get("/")
def root():
    return {"message": "Welcome to JoshLePresta API."}
