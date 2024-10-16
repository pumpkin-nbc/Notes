# mongo

```shell
docker run -d \
           --name mongo \
           --restart=always  \
           -p 27017:27017 \
           -v /etc/localtime:/etc/localtime \
           -v /etc/localtime:/etc/timezone \
           -e TZ=Asia/Shanghai \
           -e MONGO_INITDB_ROOT_USERNAME=mongo \
           # 设置数据库root的密码 可以选择使用file文件传入 两个变量二选一即可 MONGO_INITDB_ROOT_PASSWORD MONGO_INITDB_ROOT_PASSWORD_FILE 设置
           -e MONGO_INITDB_ROOT_PASSWORD=mongo \
           -e MONGO_INITDB_ROOT_PASSWORD_FILE=/run/secrets/mongo-root \
           -v /data/docker/mongo/data:/data/db \
           -v /data/docker/mongo/conf/mongod.conf:/etc/mongo/mongod.conf \
           -v /data/docker/mongo/logs:/var/log/mongodb \
           mongo:latest --config /etc/mongo/mongod.conf
```

```shell
# mongod.conf

# 有关所有选项的文档，请参阅:
#   http://docs.mongodb.org/manual/reference/configuration-options/

# 存储数据的位置和方式.
storage:
  dbPath: /data/db
  #engine:
  #wiredTiger:

# 在何处写入日志记录数据.
systemLog:
  destination: file
  logAppend: true
  path: /var/log/mongodb/mongod.log

# 网络接口
net:
  port: 27017
  bindIp: 0.0.0.0


# 流程如何运行
processManagement:
  # 设置时区
  timeZoneInfo: /usr/share/zoneinfo
  # 设置进程为守护进程
  fork: false

#security:

#operationProfiling:

#replication:

#sharding:

#Enterprise-Only Options:

#auditLog:
```