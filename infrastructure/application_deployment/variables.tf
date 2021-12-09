variable "name" {
  type        = string
  description = "Name tag"
  default     = "factorial-app"
}

variable "environment" {
  type        = string
  description = "Environment tag"
  default     = "Development"
}

variable "cluster_name" {
  type        = string
  description = "Cluster name"
  default     = "container-app"
}