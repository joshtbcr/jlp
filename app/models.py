from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    cedula = Column(String, unique=True, index=True)
    contrasena = Column(String)
    cuentas = relationship("Cuenta", back_populates="usuario")
    permiso = Column(Integer, default=1)

class Cuenta(Base):
    __tablename__ = "cuentas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_cedula = Column(String, ForeignKey("usuarios.cedula"),nullable=False)
    moneda = Column(String)
    balance = Column(Float, default=0.0)
    prestamo_id = Column(Integer, ForeignKey("prestamos.id"), nullable=True)
    usuario = relationship("Usuario", back_populates="cuentas")
    prestamo = relationship("Prestamo")
    movimientos = relationship("Movimiento")

class Prestamo(Base):
    __tablename__ = "prestamos"
    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Float)
    interes_anual = Column(Float)
    plazo_meses = Column(Integer)
    fecha_inicio = Column(DateTime, default=datetime.utcnow)
    dia_cargo_interes = Column(Integer, default=1)
    morosidad = Column(Boolean, default=False)
    moneda = Column(String)
    cuenta = relationship("Cuenta", uselist=False, back_populates="prestamo")

class Movimiento(Base):
    __tablename__ = "movimientos"
    id = Column(Integer, primary_key=True, index=True)
    cuenta_id = Column(Integer, ForeignKey("cuentas.id"))
    tipo = Column(String)
    usuarioRegistrante_cedula = Column(String, ForeignKey("usuarios.cedula"),nullable=False)
    usuarioRegistrante = relationship("Usuario")
    monto = Column(Float)
    detalle = Column(String)
    fecha = Column(DateTime, default=datetime.utcnow)
    blob_url = Column(String, nullable=True)
    # cuenta = relationship("Cuenta", back_populates="movimientos")