#ON Local

## Download minikube and start 

minikube start
minikube dashboard


### Deploying RabbitMQ:
kubectl create -f ./infra/rabbitmq/

### Deploying Redis:
kubectl apply -f ./infra/redis/



### Listing pods on cluster:
kubectl get pods --all-namespaces


## Getting logs of application labels
kubectl logs -lapp=taskQueue



##Listing all pods
kubectl get pod 

## Shell on a container
kubectl exec -it rabbitmq-controller-vqxxq -- /bin/sh