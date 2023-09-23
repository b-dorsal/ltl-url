# Project Setup Vars
########################################
environment         = "dev"
project_id          = "gke-example"
billing_account_id  = "Dataflow Tutorials"

enabled_services    = [ 
    "container.googleapis.com",
    "iam.googleapis.com",
    "monitoring.googleapis.com",
    "logging.googleapis.com",
    "compute.googleapis.com"
]


# GKE Cluster Vars
########################################

kubernetes_version  = "1.27"

cluster_zone        = "us-central1-b"

cluster_name        = "flask-app-cluster" # "ltlurl-cluster"

init_node_count     = 2

machine_type        = "n1-standard-4"