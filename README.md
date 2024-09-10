## Create VENT

python3 -m venv venv


### Run for VENV

.\venv\Scripts\Activate.ps1


## Install packages

py -m pip install -r requirements.txt

pydantic-settings
pip install python-multipart
pip install sqlalchemy-utils
pip install pandas

# One or the other
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

##  password is password

remove

2>15


