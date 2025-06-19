output "ml_app_url" {
  value = "http://${azurerm_container_group.ml_app.fqdn}"
}