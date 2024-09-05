import openpyxl.writer
import openpyxl.writer.excel
from .. import models,schemas, auth
from app.crud import cuentaCRUD
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional
import io
import pandas
import openpyxl
from openpyxl.styles import PatternFill
import base64

router = APIRouter(
    prefix='/cuentas',
    tags=['Cuentas']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Cuenta)
def create_cuenta(cuentaACrear: schemas.CuentaCreate, db: Session = Depends(get_db)):
    
    ## Permiso 0 = admin
    ## Permiso 1 = normal
    raise HTTPException (status_code=status.HTTP_306_RESERVED,
                        detail=f"Cuenta se crea con la creacion de un prestamo.")
    if usuarioExistente is not None:
        print(f"Usuario ya existe: {usuarioExistente}")

    cuentaACrear = cuentaCRUD.create_cuenta(db, usuario)
    print(f"Usuario creado: {nuevo_usuario}")

    return nuevo_usuario


@router.get("/",response_model=List[schemas.Cuenta])
def get_cuentas(db: Session = Depends(get_db),
                id_usuario: Optional[str] = ""):


    cuentas_existentes = cuentaCRUD.get_cuentas(db, id_usuario)
    print(f"==>> cuentas_existentes: {cuentas_existentes}")

    if not cuentas_existentes:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No hay cuentas existentes.")
    
    return cuentas_existentes


@router.get("/generate-excel/",response_model=schemas.ExcelResponse)
def get_cuentas(db: Session = Depends(get_db),
                id_usuario: Optional[str] = ""):

    cuentas_existentes = cuentaCRUD.get_cuentas(db, id_usuario)[0]
    print(f"==>> cuentas_existentes: {cuentas_existentes}")

    if not cuentas_existentes:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No hay cuentas existentes.")
    
    #######
    nombreSheet = "Estado de Cuenta - Prestamo"
    nombreArchivo = "EstadoDeCuenta.xlsx"

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = nombreSheet
    
    ws.append(["Name", "Age", "Occupation"])
    for name, age, occupation in zip(["Josh"], ["30"], ["Engineer"]):
        ws.append([name, age, occupation])
    
    # Save the workbook to an in-memory file
    output = io.BytesIO() 
    wb.save(output)
    output.seek(0)

    openpyxl.writer.excel.save_workbook(wb)
    # wb.save(nombreArchivo)
    print(f"==>> output: {output.getvalue()}")
    
    # Base64 encode the file content
    file_content = base64.b64encode(output.read()).decode('utf-8')

    headers = {
        'Content-Disposition': f'attachment; filename="{nombreArchivo}"'
    }

    return StreamingResponse(output, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', headers=headers, as_attachment=True)
    
''' 
@router.get("/generate-excel/",response_model=schemas.ExcelData)
def get_cuentas(db: Session = Depends(get_db),
                id_usuario: Optional[str] = ""):

    cuentas_existentes = cuentaCRUD.get_cuentas(db, id_usuario)[0]
    print(f"==>> cuentas_existentes: {cuentas_existentes}")

    if not cuentas_existentes:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No hay cuentas existentes.")
    

    df = pandas.DataFrame({
        "Name": ["Josh"],
        "Age": ["30"],
        "Occupation": ["Engineer"]
    })
    nombreSheet = "Estado de Cuenta - Prestamo"
    nombreArchivo = "EstadoDeCuenta.xlsx"
    
    # Save the DataFrame to an Excel file in memory
    output = io.BytesIO()
    with pandas.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name=f'{nombreSheet}')
    
    output.seek(0)
    headers = {
        'Content-Disposition': f'attachment; filename="{nombreArchivo}"'
    }
    return StreamingResponse(output, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', headers=headers)
''' 