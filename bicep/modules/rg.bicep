param rgConfig object
targetScope = 'subscription'

resource rg 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: rgConfig.name
  location: rgConfig.location
}
output resourceGroupName string = rg.name
// az deployment sub create --location eastus2 --template-file ./bicep/modules/rg.bicep
