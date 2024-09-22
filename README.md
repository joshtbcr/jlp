## Create VENT

python3 -m venv venv


### Run for VENV

.\venv\Scripts\Activate.ps1


## Install packages

py -m pip install -r requirements.txt


### These are now added--- cehcking if it works
pydantic-settings
pip install python-multipart
pip install sqlalchemy-utils
pip install pandas
pip install xlsxwriter
pip install openpyxl


### Disable postgres from running auto in windows

Set-Service -Name "postgresql-x64-16" -StartupType Manual


### Stop/Start postgres

# Stop the PostgreSQL service
Stop-Service -Name "postgresql-x64-16" -Force
Start-Service -Name "postgresql-x64-16"

Get-Service -Name "postgresql-x64-16"
## How to run the server

uvicorn app.main:app --reload

##Summary

.\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload

##  DB password is password

### Docker instructions

#### Create docker image
docker build -t jlp-dev1 .

#### Create container from docker image in docker compose
docker-compose up -d


####Working on stuff,, not formal

predev

DB_USER=postgres
DB_PASS=password
DB_HOST=jlb-predev.postgres.database.azure.com
DB_NAME=jlp
SECRET_KEY=f9c7deb65801fdfa6895b9fd8e7995618ba8c49670774cf8821a3debd28f42c3
NOMBRE_EMPRESA=Josh Le Presta
NOMBRE_ARCHIVO_CUENTA_EXCEL=estado_de_cuenta