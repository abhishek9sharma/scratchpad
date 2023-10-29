
docker stop $(docker ps|grep kubefastapiapp| awk '{print $1}')
docker container rm $(docker container ls -a|grep kubefastapiapp| awk '{print $1}')
docker image rm $(docker images|grep kubefastapiapp| awk '{print $3}')
docker build --tag kubefastapiapp .
docker run -p 80:80 kubefastapiapp