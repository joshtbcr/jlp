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
docker build -t jlp-dev .

#### Create container from docker image in docker compose
docker-compose up -d

#### ACR Login

az login --use-device-code --tenant 3cc1100c-611d-4789-9330-4d161e8eef07
az acr login --name jlppredev


### Testing only docker ms image
docker pull mcr.microsoft.com/mcr/hello-world
docker tag mcr.microsoft.com/mcr/hello-world jlppredev.azurecr.io/samples/hello-world

docker push jlppredev.azurecr.io/samples/hello-world