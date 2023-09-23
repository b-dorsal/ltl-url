data "google_container_engine_versions" "supported" {
  location          = var.cluster_zone
  version_prefix    = var.kubernetes_version
  project           = google_project.gke_project.project_id
}

resource "google_container_cluster" "default" {
  project               = google_project.gke_project.project_id
  name                  = var.cluster_name
  location              = var.cluster_zone
  initial_node_count    = var.init_node_count
  min_master_version    = data.google_container_engine_versions.supported.latest_master_version

  node_version          = data.google_container_engine_versions.supported.latest_master_version

#   node_locations = [
#     var.cluster_zone
#   ]

  node_config {
    machine_type        = var.machine_type

    oauth_scopes = [
      "https://www.googleapis.com/auth/compute",
      "https://www.googleapis.com/auth/devstorage.read_only",
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]
  }
}


#  Ingress Static IP
resource "google_compute_global_address" "default" {
  name      = var.lb_ip_name
  project   = google_project.gke_project.project_id
}