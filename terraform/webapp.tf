resource "azurerm_service_plan" "asp" {
  name                = "${var.projectName}-ASP"
  resource_group_name = azurerm_resource_group.baseRG.name
  location            = azurerm_resource_group.baseRG.location
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "web_app" {
  name                = "${var.projectName}-APP"
  resource_group_name = azurerm_resource_group.baseRG.name
  location            = azurerm_resource_group.baseRG.location
  service_plan_id     = azurerm_service_plan.asp.id

  app_settings = {
  }

  site_config {
    always_on = true
    application_stack {
      python_version = "3.10"
    }
  }

  lifecycle {
    ignore_changes = [
      tags,
      app_settings["WEBSITES_ENABLE_APP_SERVICE_STORAGE"],
      app_settings["WEBSITE_ENABLE_SYNC_UPDATE_SITE"],
      site_config["application_stack"]
    ]
  }

}