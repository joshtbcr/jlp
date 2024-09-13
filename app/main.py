from fastapi import FastAPI #, Depends
from app import models
from app.routers import auth #, crud,  database
from .routers import usuario, cuenta, movimiento, prestamo
from app.database import engine
# from app.dependencies import get_db
from fastapi.middleware.cors import CORSMiddleware



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Rutas de autenticación
app.include_router(auth.router)
app.include_router(usuario.router)
app.include_router(prestamo.router)
app.include_router(cuenta.router)
app.include_router(movimiento.router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to JoshLePresta API."}
