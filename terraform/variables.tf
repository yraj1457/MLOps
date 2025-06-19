variable "location" {
  default = "East US"
}

variable "container_image" {
  description = "Docker image to deploy"
  type        = string
}

variable "dns_label" {
  description = "DNS prefix for public IP"
  type        = string
}