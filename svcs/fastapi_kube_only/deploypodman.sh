
podman stop $(podman ps|grep kubefastapiapp| awk '{print $1}')
podman container rm $(podman container ls -a|grep kubefastapiapp| awk '{print $1}')
podman image rm $(podman images|grep kubefastapiapp| awk '{print $3}')
podman build --tag kubefastapiapp .
podman run -p 80:80 kubefastapiapp