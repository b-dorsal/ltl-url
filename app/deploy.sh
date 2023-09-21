
cd ../k8s/

kubectl delete -f flask-app.yaml

cd ../app/

docker build -t bdor528/ltl-url .

docker push bdor528/ltl-url

cd ../k8s/

kubectl apply -f flask-app.yaml

cd ../app/

sleep 5

app_pod=$(kubectl get pods -o NAME | grep flask-app-deployment)
echo $app_pod
kubectl logs $app_pod