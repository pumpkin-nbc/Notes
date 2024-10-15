# portainer
```shell
# 可选普通版 portainer/portainer-ce:latest 企业版 portainer/portainer-ee:latest
# http部署
docker run -d \
           --name portainer \
           --restart=always \
           -p 8000:8000 \
           -p 9000:9000 \
           -e TZ=Asia/Shanghai \
           -v /var/run/docker.sock:/var/run/docker.sock \
           -v /data/portainer/data:/data \
           portainer/portainer-ee:latest
# https部署
docker run -d \
           --name portainer \
           --restart=always \
           -p 8000:8000 \
           -p 9443:9443 \
           -e TZ=Asia/Shanghai \
           -v /var/run/docker.sock:/var/run/docker.sock \
           -v /data/portainer/data:/data \
           -v /data/portainer/certs:/certs \
           portainer/portainer-ee:latest --sslcert /certs/a.crt --sslkey /certs/a.key
```