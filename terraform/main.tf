resource "azurerm_resource_group" "baseRG" {
  name     = var.projectName
  location = "East US"
}
