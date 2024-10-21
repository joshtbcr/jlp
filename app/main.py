from fastapi import FastAPI
import uvicorn #, Depends
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
    "file:///C:/Users/jotorres/Repos/jlp-load-beforenpm/jlp/frontend/index.html",
    "https://orange-mud-0d3cbdd0f.5.azurestaticapps.net", #predev2
    "null", # Don't leave in prod,  just to allow local files as origins
    "http://localhost",
    "http://localhost:8080",
    "https://dev.joshlepresta.com",
    "https://joshlepresta.com",
    "https://www.joshlepresta.com",
    "https://64d0-170-246-157-55.ngrok-free.app"
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

