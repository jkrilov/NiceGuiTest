data "azurerm_client_config" "current" {}

resource "azurerm_key_vault" "nicegui" {
  name                       = "${var.projectName}-KV"
  location                   = azurerm_resource_group.baseRG.location
  resource_group_name        = azurerm_resource_group.baseRG.name
  tenant_id                  = data.azurerm_client_config.current.tenant_id
  soft_delete_retention_days = 7
  purge_protection_enabled   = false

  sku_name = "standard"

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id

    secret_permissions = [
      "Get",
      "List",
      "Set",
      "Delete",
      "Purge"
    ]

  }
}

resource "azurerm_key_vault_secret" "aca-url" {
  name         = "aca-url"
  value        = azurerm_container_registry.nicegui.login_server
  key_vault_id = azurerm_key_vault.nicegui.id
}

resource "azurerm_key_vault_secret" "aca-user" {
  name         = "aca-user"
  value        = azurerm_container_registry.nicegui.admin_username
  key_vault_id = azurerm_key_vault.nicegui.id
}

resource "azurerm_key_vault_secret" "aca-pass" {
  name         = "aca-pass"
  value        = azurerm_container_registry.nicegui.admin_password
  key_vault_id = azurerm_key_vault.nicegui.id
}