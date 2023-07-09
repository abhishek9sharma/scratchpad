minikube addons enable ingress 
#minikube  dashboard --url
#minikube tunnel

eval $(minikube docker-env)
docker stop $(docker ps|grep kubefastapiapp| awk '{print $1}')
docker container rm $(docker container ls -a|grep kubefastapiapp| awk '{print $1}')
docker image rm $(docker images|grep kubefastapiapp| awk '{print $3}')
docker build --tag kubefastapiapp .
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml


#LINKS
#https://richard.to/programming/hello-world-fast-api-kubenetes.html
#https://www.youtube.com/watch?v=WC4e3Yq8k8A
#https://www.youtube.com/watch?v=i7PFg6aVcdI