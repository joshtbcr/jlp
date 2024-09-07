from typing import List
from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime
from app.config import settings

import openpyxl.writer
import openpyxl.writer.excel
import io
import pandas
import openpyxl
from openpyxl.styles import PatternFill,Font, Alignment


def create_cuenta(db: Session, prestamo: schemas.Prestamo, usuario_id: str):
    
    id_usuario = str(db.query(models.Usuario).filter(models.Usuario.id_usuario == str(usuario_id)).first().id)
    print(f"==>> id_usuario: {id_usuario}")

    
    cuenta = schemas.CuentaCreate(
        prestamo_id=prestamo.id,
        moneda=prestamo.moneda,
        balance=prestamo.monto,
        usuario_id=id_usuario
    )
    db_cuenta = models.Cuenta(**cuenta.dict())

    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta


def get_cuentas(db: Session, id_usuario):
    #TODO
    permiso_usuario = 0
    
    print(f"==>> id_usuario: {id_usuario}")
    if id_usuario == "":
        if permiso_usuario == 0:
            cuentas_existentes = db.query(models.Cuenta).all()
            return cuentas_existentes   
        elif permiso_usuario > 0:
            cuentas_existentes = List[schemas.Cuenta]
            return cuentas_existentes
    else:   
        print(f"==>>Obteniendo todas las cuestas del usuario: {id_usuario}")
        cuentas_existentes = db.query(models.Cuenta).filter(models.Cuenta.usuario_id == id_usuario).all()
        return cuentas_existentes   
    
    return db.query(models.Cuenta).all()

def get_cuentaExcel(db: Session, usuario_id_usuario):
    #TODO
    permiso_usuario = 0

    print(f"==>>Obteniendo todas las cuestas del usuario: {usuario_id_usuario}")
    cuentas_existentes: schemas.CuentaExcel = db.query(models.Cuenta).filter(models.Cuenta.usuario_id == usuario_id_usuario).first()
    return cuentas_existentes   


def get_Excel(db: Session, output, usuario_id_usuario):

    cuenta: schemas.CuentaExcel = get_cuentaExcel(db, usuario_id_usuario)
    
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Estado de Cuenta"

    # Añadir título del documento (Nombre de la empresa y nombre del cliente)
    ws.merge_cells('A1:E1')
    ws['A1'] = f"Estado de Cuenta - {settings.NOMBRE_EMPRESA}"
    ws['A1'].font = Font(bold=True, size=14)
    ws['A1'].alignment = Alignment(horizontal="center")
    
    ws.merge_cells('A2:E2')
    ws['A2'] = f"Cliente: {cuenta.usuario.nombre}"
    ws['A2'].font = Font(bold=True, size=12)
    ws['A2'].alignment = Alignment(horizontal="center")

    # Definir el color de la cabecera
    header_fill = PatternFill(start_color="00CCFF99", end_color="00CCFF99", fill_type="solid")  # Verde claro
    header_font = Font(bold=True, color="FFFFFF")  # Blanco para el texto

    # Añadir las cabeceras con fondo verde
    headers = ["Fecha", "Tipo","Detalle", "Monto", "Balance", "Realizado por"]
    ws.append(headers)

    for col in range(1, len(headers) + 1):
        cell = ws.cell(row=4, column=col)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")

    # Establecer el ancho de las columnas
    ws.column_dimensions['A'].width = 28  # Columna para Fecha
    ws.column_dimensions['B'].width = 28  # Columna para Detalle

    # Agregar movimientos a la tabla
    movimientos = [{"date": "2024-09-06","tipo":"Crédito", "detail": "Pago préstamo", "amount": -100, "balance": 900, "usuario":"Jane Berrocal"}]
    for movement in movimientos:
        ws.append([
            movement["date"],
            movement["tipo"],
            movement["detail"],
            movement["amount"],
            movement["balance"],
            movement["usuario"]
        ])

    # Guardar el archivo en memoria
    wb.save(output)
    output.seek(0)
    return output