from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class MovimientoBase(BaseModel):
    tipo: str
    monto: float
    detalle: str
    blob_url: Optional[str] = None

class MovimientoCreate(MovimientoBase):
    pass

class Movimiento(MovimientoBase):
    id: int
    cuenta_id: int
    fecha: datetime

    class Config:
        orm_mode = True

class PrestamoBase(BaseModel):
    monto: float
    interes_anual: float
    plazo_meses: int
    moneda: str

class PrestamoCreate(PrestamoBase):
    pass

class Prestamo(PrestamoBase):
    id: int
    fecha_inicio: datetime
    fecha_cargo_interes: datetime
    morosidad: bool

    class Config:
        orm_mode = True

class CuentaBase(BaseModel):
    moneda: str

class CuentaCreate(CuentaBase):
    prestamo: PrestamoCreate

class Cuenta(CuentaBase):
    id: int
    balance: float
    cliente_id: int
    movimientos: List[Movimiento] = []

    class Config:
        orm_mode = True

class ClienteBase(BaseModel):
    nombre: str
    id_cliente: str

class ClienteCreate(ClienteBase):
    contrasena: str

class Cliente(ClienteBase):
    id: int
    cuentas: List[Cuenta] = []

    class Config:
        orm_mode = True
