from fastapi import Depends, HTTPException, Response, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app import models, schemas, crud
from app.database import get_db
from app.config import settings

# Configuración para hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


router = APIRouter(tags=['Authentication'])

# Configuración para JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(db: Session, cedula: str, password: str):
    user = db.query(models.Usuario).filter(models.Usuario.cedula == cedula).first()
    if not user:
        return False
    if not verify_password(password, user.contrasena):
        return False
    return user

def create_access_token(data: dict):
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta

    to_encode = data.copy()
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Ruta para obtener token
@router.post("/token", response_model=schemas.Token)
def login_for_access_token(response: Response,form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrecta.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    jwtPayload = {
        "sub": user.cedula,
        "user_name": user.nombre,
        "role": user.permiso
    }

    access_token = create_access_token(data=jwtPayload)
    response.set_cookie(key="jwt_token", 
                        value=access_token,
                        # domain=domainAPI,
                        #   httponly=True,
                          secure=True,
                          samesite="None",
                          max_age=5260032, # two months
                          domain=".joshlepresta.com"  # This allows the cookie to be shared across subdomains
                        )
    return {"access_token": access_token, "token_type": "bearer"}

def hash(password:str):
    return pwd_context.hash(password)