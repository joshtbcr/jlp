from pydantic import BaseModel, field_serializer
from datetime import datetime
from typing import List, Optional

class MovimientoBase(BaseModel):
    tipo: str
    monto: float
    detalle: str
    cuenta_id: int
    usuarioRegistrante_id: int
    blob_url: Optional[str] = None

class MovimientoCreate(MovimientoBase):
    pass

class Movimiento(MovimientoBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True

class PrestamoBase(BaseModel):
    monto: float
    interes_anual: float
    plazo_meses: int
    moneda: str

class PrestamoCreate(PrestamoBase):
    dia_cargo_interes: int = 1
    usuario_id: int
    pass

class PrestamoInput(PrestamoCreate):
    usuario_id: int
    pass

class Prestamo(PrestamoBase):
    id: int
    fecha_inicio: datetime = None
    dia_cargo_interes: int
    morosidad: bool

    class Config:
        orm_mode = True

class CuentaBase(BaseModel):
    moneda: str
    balance: float
    usuario_id: str | int
    prestamo_id: int
    
    @field_serializer("usuario_id")
    def serialize_usuario_id(self, usuario_id: str | int, _info):
        return str(usuario_id)

class CuentaCreate(CuentaBase):
    pass

class Cuenta(CuentaBase):
    id: int
    movimientos: List[Movimiento] = []
    prestamo: Prestamo

    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    nombre: str
    permiso: int = 1
    id_usuario: str

class UsuarioCreate(UsuarioBase):
    contrasena: str

class Usuario(UsuarioBase):
    id: int
    cuentas: List[Cuenta] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id_cliente: Optional[str] = None

class CuentaExcel(CuentaBase):
    id: int
    movimientos: List[Movimiento] = []
    usuario: Usuario
    prestamo: Prestamo

    class Config:
        orm_mode = True


# Pydantic model for the input data
class ExcelResponse(BaseModel):
    filename: str
    file_content: str  # Base64 encoded content of the file