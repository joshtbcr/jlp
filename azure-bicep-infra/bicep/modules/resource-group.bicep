module rgModule 'modules/resource-group.bicep' = {
  name: 'createResourceGroup'
  params: {
    name: 'jlp-predev-rg'
    location: 'eastus'
  }
}