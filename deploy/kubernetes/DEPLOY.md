#ON Local

## Download minikube and start 

minikube start
minikube dashboard


Deploying RabbitMQ:
kubectl create -f ./infra/rabbitmq/

Deploying Redis:
kubectl apply -f ./infra/redis/



Listing pods on cluster:
kubectl get pods --all-namespaces



