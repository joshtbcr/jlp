from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    id_cliente = Column(String, unique=True, index=True)
    contrasena = Column(String)
    cuentas = relationship("Cuenta", back_populates="cliente")

class Cuenta(Base):
    __tablename__ = "cuentas"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    moneda = Column(String)
    balance = Column(Float, default=0.0)
    prestamo_id = Column(Integer, ForeignKey("prestamos.id"))
    cliente = relationship("Cliente", back_populates="cuentas")
    movimientos = relationship("Movimiento", back_populates="cuenta")

class Prestamo(Base):
    __tablename__ = "prestamos"
    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Float)
    interes_anual = Column(Float)
    plazo_meses = Column(Integer)
    fecha_inicio = Column(DateTime, default=datetime.utcnow)
    fecha_cargo_interes = Column(DateTime)
    morosidad = Column(Boolean, default=False)
    moneda = Column(String)
    cuenta = relationship("Cuenta", uselist=False, back_populates="prestamo")

class Movimiento(Base):
    __tablename__ = "movimientos"
    id = Column(Integer, primary_key=True, index=True)
    cuenta_id = Column(Integer, ForeignKey("cuentas.id"))
    tipo = Column(String)
    monto = Column(Float)
    detalle = Column(String)
    fecha = Column(DateTime, default=datetime.utcnow)
    blob_url = Column(String, nullable=True)
    cuenta = relationship("Cuenta", back_populates="movimientos")