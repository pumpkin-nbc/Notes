# dashy

* 导航页面

```shell
# http访问配置
docker run -d \
           --name dashy \
           --restart=always \
           -p 8080:8080 \
           -v /etc/localtime:/etc/localtime \
           -v /etc/localtime:/etc/timezone \
           -v /data/dashy/conf/conf.yml:/app/user-data/conf.yml \
           -e TZ=Asia/Shanghai \
           lissy93/dashy:latest
           
# https访问配置
docker run -d \
           --name dashy \
           --restart=always \
           -p 443:443 \
           -v /etc/localtime:/etc/localtime \
           -v /etc/localtime:/etc/timezone \
           -v /data/dashy/conf/conf.yml:/app/user-data/conf.yml \
           -v /data/dashy/certs:/certs \
           -e SSL_PRIV_KEY_PATH='/certs/dashy-priv.key' \
           -e SSL_PUB_KEY_PATH='/certs/dashy-pub.pem' \
           -e TZ=Asia/Shanghai \
           lissy93/dashy:latest
```

