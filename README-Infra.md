#### ACR Login
az login --use-device-code --tenant 3cc1100c-611d-4789-9330-4d161e8eef07
az acr login --name jlppredev

### Push image to ACR
#### Create a tag
docker tag jlp-api jlppredev.azurecr.io/jlp-api-dev 
#### Push that tag
docker push jlppredev.azurecr.io/jlp-api-dev

#####  Webapp
az webapp config appsettings set --resource-group jlp-predev-rg --name webapp-jlp-dev  --settings WEBSITES_PORT=8000

####


az deployment group create --name DeployWebApp --resource-group jlp-predev-rg
 --template-file 




#####  Webapp
az webapp config appsettings set --resource-group jlp-predev-rg --name webapp-jlp-dev  --settings WEBSITES_PORT=8000

##### Steps to load SSL into local FastAPI

nano openssl.cnf
openssl genrsa -out key.pem 2048
openssl req -x509 -new -nodes -key key.pem -sha256 -days 365 -out cert.pem -config openssl.cnf

## PFX
openssl pkcs12 -export -out cert.pfx -inkey key.pem -in cert.pem