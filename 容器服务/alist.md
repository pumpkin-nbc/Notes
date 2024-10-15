# alist
```shell
docker run -d \
           --name=alist \
           --restart=always \
           -v /etc/localtime:/etc/localtime \
           -v /etc/localtime:/etc/timezone \
           -v /data/alist/data:/opt/alist/data \
           -p 5244:5244 \
           -e PUID=0 -e PGID=0 -e UMASK=022 \
           -e TZ=Asia/Shanghai \
           xhofe/alist-aria2:latest
```