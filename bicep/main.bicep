// #1 Create RG
// #2 Create DB
// #3 Create ACR
// #4 Create AppService
// #5 Create SWA (Different sub though)



module rgModule 'modules/resource-group.bicep' = {
  name: 'createResourceGroup'
  params: {
    name: 'jlp-dev-rg'
    location: 'eastus'
  }
