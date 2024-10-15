# minio

```shell
docker run -d \
           --name minio \
           --restart=always \
           -v /etc/localtime:/etc/localtime \
           -v /etc/localtime:/etc/timezone \
           -p 9000:9000 \
           -p 9001:9001 \
           -v /data/MinIO:/data \
           -v /data/docker/minio/certs:/certs \
           -v /data/docker/minio/config/minio.conf:/etc/config.env \
           -e "MINIO_CONFIG_ENV_FILE=/etc/config.env" \
           -e TZ=Asia/Shanghai \
           minio/minio:latest server /mnt/data --certs-dir /certs --console-address ":9001"
```

```text
# minio.conf

# MINIO_ROOT_USER和MINIO_ROOT_PASSWORD设置MINIO服务器的根帐户。
# 此用户具有对部署中的任何资源执行S3和管理API操作的不受限制的权限。
# 省略使用默认值“minioadmin:minioadmin”。
# MinIO建议将非默认值设置为最佳实践，无论环境如何。

MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=minioadmin

# MINIO_VOLUMES设置用于MINIO服务器的存储卷或路径。
# 扩展驱动器列表中包含的所有驱动器或路径必须存在*并且*为空或新格式化，以便MinIO成功启动。

MINIO_VOLUMES="/mnt/data"

# MINIO_OPTS设置要传递给MINIO服务器的任何其他命令行选项。
# 例如， `--address :9000` 设置MinIO的api端口 `--console-address :9001` 设置MinIO的web端口
# 此处指定了api服务的端口 web服务的端口
MINIO_OPTS="--address :9000 --console-address :9001 --certs-dir /certs"

# 设置minio https的api端口 9000 web服务端口 9001
MINIO_SERVER_URL="https://域名:9000"
MINIO_BROWSER_REDIRECT_URL="https://域名:9001"

# 设置s3的注册地址
MINIO_REGION_NAME="zh-east-1"
MINIO_REGION_COMMENT="China"


```