# ltl-url
A containerized tiny url shortening service

## Usage

#### Deploy to the GKE cluster

Create Infrastructure
```bash
cd terraform
terraform init
terraform plan -var-file=envvars/dev.tfvars
terraform apply -var-file=envvars/dev.tfvars
```

Get the cluster credentials
```bash
gcloud container clusters get-credentials ltlurl-cluster --region=us-central1-b
```

Deploy our config - still havent made this into a Helm chart
Not deploying mongo-express
```bash
kubectl apply -f namespace.yaml
kubectl apply -f mongo-secret.yaml
kubectl apply -f mongo-configmap.yaml
kubectl apply -f mongo.yaml
kubectl apply -f flask-app.yaml
kubectl apply -f flask-ingress.yaml
```

Wait for an IP on ingress, and visit in a browser
```bash
kubectl get flask-ingress -n flask-app-ns
```