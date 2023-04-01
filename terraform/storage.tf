resource "azurerm_storage_account" "storage_account" {
  name                     = "${lower(var.projectName)}sa"
  resource_group_name      = azurerm_resource_group.baseRG.name
  location                 = azurerm_resource_group.baseRG.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}