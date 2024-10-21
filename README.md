## Create VENT

python3 -m venv venv
or
py -m venv venv


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

## Summary

.\venv\Scripts\Activate.ps1

uvicorn main:app 


## Load with HTTPS
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000 --ssl-keyfile="C:\\Users\\jotorres\\Repos\\jlp-with-bicepnotworking\\jlp\\app\\ssl\\key.pem" --ssl-certfile="C:\\Users\\jotorres\\Repos\\jlp-with-bicepnotworking\\jlp\\app\\ssl\\cert.pem"


##  DB password is password

### Docker instructions

#### Create docker image (I think not needed because compose creates image again)
docker build -t jlp-dev .

#### Create container from docker image in docker compose
docker-compose up -d

#### ACR Login
az login --use-device-code --tenant 3cc1100c-611d-4789-9330-4d161e8eef07
az acr login --name jlppredev

### Push image to ACR
#### Create a tag
docker tag jlp-api jlppredev.azurecr.io/jlp-api-dev 
#### Push that tag
docker push jlppredev.azurecr.io/jlp-api-dev


