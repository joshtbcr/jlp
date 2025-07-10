module rgModule 'modules/resource-group.bicep' = {
  name: 'createResourceGroup'
  params: {
    name: 'jlp-dev-rg'
    location: 'eastus'
  }