provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "ml_rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_container_group" "ml_app" {
  name                = "ml-model-api"          
  location            = azurerm_resource_group.ml_rg.location
  resource_group_name = azurerm_resource_group.ml_rg.name
  os_type             = "Linux"

  container {
    name   = "mlmodel"
    image  = var.container_image
    cpu    = "1.0"
    memory = "1.5"

    ports {
      port     = 80
      protocol = "TCP"
    }
  }

  ip_address_type = "public"
  dns_name_label  = var.dns_label
}
