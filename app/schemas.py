from pydantic import BaseModel, ConfigDict, field_serializer
from datetime import datetime
from typing import List, Optional

class MovimientoBase(BaseModel):
    tipo: str
    monto: float
    detalle: str
    cuenta_id: int
    usuarioRegistrante_cedula: str
    blob_url: Optional[str] = None

class MovimientoCreate(MovimientoBase):
    pass

class Movimiento(MovimientoBase):
    id: int
    fecha: datetime

    model_config = ConfigDict(from_attributes=True)

class PrestamoBase(BaseModel):
    monto: float
    interes_anual: float
    plazo_meses: int
    moneda: str

class PrestamoCreate(PrestamoBase):
    dia_cargo_interes: int = 1
    usuario_cedula: str
    pass

class PrestamoInput(PrestamoCreate):
    usuario_cedula: str
    pass

class Prestamo(PrestamoBase):
    id: int
    fecha_inicio: datetime = None
    dia_cargo_interes: int
    morosidad: bool

    model_config = ConfigDict(from_attributes=True)

class CuentaBase(BaseModel):
    moneda: str
    balance: float
    usuario_cedula: str | int
    prestamo_id: int
    
    @field_serializer("usuario_cedula")
    def serialize_usuario_cedula(self, usuario_cedula: str | int, _info):
        return str(usuario_cedula)

class CuentaCreate(CuentaBase):
    pass

class Cuenta(CuentaBase):
    id: int
    movimientos: List[Movimiento] = []
    prestamo: Prestamo
    model_config = ConfigDict(from_attributes=True)

class UsuarioBase(BaseModel):
    nombre: str
    permiso: int = 1
    cedula: str

class UsuarioCreate(UsuarioBase):
    contrasena: str

class Usuario(UsuarioBase):
    id: int
    cuentas: List[Cuenta] = []
    model_config = ConfigDict(from_attributes=True)

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
    model_config = ConfigDict(from_attributes=True)




# Pydantic model for the input data
class ExcelResponse(BaseModel):
    filename: str
    file_content: str  # Base64 encoded content of the file

class MovimientoExcel(MovimientoBase):
    id: int
    fecha: datetime
    usuarioRegistrante_id: Usuario
    balance: int

    model_config = ConfigDict(from_attributes=True)