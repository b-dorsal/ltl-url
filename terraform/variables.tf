
# Project Setup Vars
########################################
variable "environment" {
    type            = string
    description     = "Environment ID"
}

variable "project_id" {
    type            = string
    description     = "ID and name of the project"
}

variable "billing_account_id" {
    type            = string
    description     = "Billing account ID"
}

variable "enabled_services" {
    type            = list(string)
    description     = "List of services/APIs to enable on the project"
}


# GKE Cluster Vars
########################################
variable "kubernetes_version" {
    type            = string
    default         = "1.18"
    description     = "Kubernetes version to use"
}

variable "cluster_zone" {
    type            = string
    default         = "us-central1-a"
    description     = "GCP zone to create our cluster in"
}

variable "cluster_name" {
    type            = string
    default         = "test-cluster"
    description     = "The name to give to the cluster"
}

variable "init_node_count" {
    type            = number
    default         = 1
    description     = "Number of initial nodes to create"
}

variable "machine_type" {
    type            = string
    default         = "n1-standard-4"
    description     = "The type of VM to use for nodes"
}