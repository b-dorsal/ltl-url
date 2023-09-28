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
kubectl apply -f mysql-secret.yaml
kubectl apply -f mysql-pv.yaml
kubectl apply -f mysql.yaml
kubectl apply -f flask-app.yaml
```

Initialize the App Database
```sql
CREATE DATABASE IF NOT EXISTS ltlurldb;
USE ltlurldb;
CREATE TABLE links (id INT NOT NULL AUTO_INCREMENT, url VARCHAR(256), uuid VARCHAR(6), PRIMARY KEY (id));
INSERT INTO links (`url`, `uuid`) VALUES ('https://www.google.com/', 'abcdef');
INSERT INTO links (`url`, `uuid`) VALUES ('https://www.facebook.com/', 'qwerty');
```

Wait for an IP on ingress, and visit in a browser
```bash
kubectl get flask-ingress
```



