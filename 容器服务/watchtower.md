# watchtower
```shell
# 每一小时检测一次容器 只需要写入容器名称到watchtower.txt文件即可
docker run -d \
           --name watchtower \
           --restart=always \
           -e TZ=Asia/Shanghai \
           -v /var/run/docker.sock:/var/run/docker.sock \
           containrrr/watchtower:latest \
           --cleanup --include-stopped --interval 3600 $(cat /data/watchtower/watchtower.txt)
```