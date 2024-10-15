# mariadb

```shell
docker run -d \
           --name mariadb \
           -p 3306:3306 \
           --restart=always \
           -v /etc/localtime:/etc/localtime \
           -v /etc/localtime:/etc/timezone \
           -e TZ=Asia/Shanghai \
           -v /data/MariaDB/data:/var/lib/mysql \
           # 映射配置文件
           -v /data/docker/mariadb/conf/mariadb.cnf:/etc/mysql/mariadb.cnf \
           # 建议设置临时密码，部署成功后修改密码 ALTER USER 'root'@'localhost' IDENTIFIED BY 'newpassword';ALTER USER 'root'@'%' IDENTIFIED BY 'newpassword';FLUSH PRIVILEGES;
           # 设置数据库root的密码 可以选择使用file文件传入 两个变量二选一即可 MARIADB_ROOT_PASSWORD_FILE MARIADB_ROOT_PASSWORD
           -e MARIADB_ROOT_PASSWORD_FILE=/run/secrets/mariadb-root
           -e MARIADB_ROOT_PASSWORD=newpassword  \
           mariadb:latest
```

```text
# mariadb.cnf
# MariaDB 配置文件
#
# MariaDB/MySQL 工具按以下顺序读取配置文件:
# 0. "/etc/mysql/my.cnf" 指向此文件的符号链接，读取其余所有内容的原因.
# 1. "/etc/mysql/mariadb.cnf" （此文件）设置全局默认值,
# 2. "/etc/mysql/conf.d/*.cnf" 设置全局选项.
# 3. "/etc/mysql/mariadb.conf.d/*.cnf" 设置仅限 MariaDB 的选项.
# 4. "~/.my.cnf" 设置用户特定的选项.
#
# 如果多次定义相同的选项，则最后一个选项将适用。
#
# 可以使用该程序支持的所有长选项。
# 使用 --help 运行 program 来获取可用选项的列表，使用 --print-defaults 来查看它实际理解和使用的选项。
#
# 如果您是 MariaDB 的新手，请查看 https://mariadb.com/kb/en/basic-mariadb-articles/

#
# 此组由客户端和服务器读取，并将其用于影响所有内容的选项
#
[client-server]
# 要连接的端口或套接字位置
# port = 3306
socket = /run/mysqld/mysqld.sock

[mariadb]
host-cache-size=0
skip-name-resolve

# 此组由客户端库读取
# 将其用于影响所有客户端的选项，但不影响服务器的选项
[client]
# 客户端证书使用示例
#ssl-cert = /etc/mysql/client-cert.pem
#ssl-key  = /etc/mysql/client-key.pem
# 仅允许 TLS 加密连接
#ssl-verify-server-cert = on

# 这个组*永远不会被 mysql 客户端库读取，尽管这个 /etc/mysql/mariadb.cnf.d/client.cnf 文件无论如何都不会被 Oracle MySQL 客户端读取.
# 如果对 MySQL 和 MariaDB 使用相同的 .cnf 文件， 将其用于仅限 MariaDB 的客户端选项
[client-mariadb]

# 这些组由 MariaDB 命令行工具读取将其用于仅影响一个实用程序的选项
[mariadb-client]

[mariadb-upgrade]

[mariadb-admin]

[mariadb-binlog]

[mariadb-check]

[mariadb-dump]

[mariadb-import]

[mariadb-show]

[mariadb-slap]

#
# 这些组由 MariaDB 服务器读取。
# 将其用于只有服务器（而不是客户端）应该看到的选项

# 它由独立守护程序和嵌入式服务器读取
[server]

# 这仅适用于 mariadbd 守护进程
[mariadbd]

#
# * 基本设置
#

#user                    = mysql
pid-file                = /run/mysqld/mysqld.pid
basedir                 = /usr
#datadir                 = /var/lib/mysql
#tmpdir                  = /tmp

# Broken reverse DNS slows down connections considerably and name resolve is
# safe to skip if there are no "host by domain name" access grants
#skip-name-resolve

# Instead of skip-networking the default is now to listen only on
# localhost which is more compatible and is not less secure.
#bind-address            = 127.0.0.1

#
# * Fine Tuning
#

#key_buffer_size        = 128M
#max_allowed_packet     = 1G
#thread_stack           = 192K
#thread_cache_size      = 8
# This replaces the startup script and checks MyISAM tables if needed
# the first time they are touched
#myisam_recover_options = BACKUP
#max_connections        = 100
#table_cache            = 64

#
# * Logging and Replication
#

# Note: The configured log file or its directory need to be created
# and be writable by the mysql user, e.g.:
# $ sudo mkdir -m 2750 /var/log/mysql
# $ sudo chown mysql /var/log/mysql

# Both location gets rotated by the cronjob.
# Be aware that this log type is a performance killer.
# Recommend only changing this at runtime for short testing periods if needed!
#general_log_file       = /var/log/mysql/mysql.log
#general_log            = 1

# Error logging goes via stdout/stderr, which on systemd systems goes to
# journald.
# Enable this if you want to have error logging into a separate file
#log_error = /var/log/mysql/error.log
# Enable the slow query log to see queries with especially long duration
#log_slow_query_file    = /var/log/mysql/mariadb-slow.log
#log_slow_query_time    = 10
#log_slow_verbosity     = query_plan,explain
#log-queries-not-using-indexes
#log_slow_min_examined_row_limit = 1000

# 以下内容可用作易于重播的备份日志或用于复制。
# note: if you are setting up a replica, see README.Debian about other
#       settings you may need to change.
#server-id              = 1
#log_bin                = /var/log/mysql/mysql-bin.log
expire_logs_days        = 10
#max_binlog_size        = 100M

#
# * SSL/TLS
#

# For documentation, please read
# https://mariadb.com/kb/en/securing-connections-for-client-and-server/
#ssl-ca = /etc/mysql/cacert.pem
#ssl-cert = /etc/mysql/server-cert.pem
#ssl-key = /etc/mysql/server-key.pem
#require-secure-transport = on

#
# * Character sets
#

# MariaDB 默认为 Latin1，但在 Debian 中，我们宁愿默认为完整的 utf8 4 字节字符集. See also client.cnf
character-set-server     = utf8mb4

#
# * InnoDB
#

# InnoDB is enabled by default with a 10MB datafile in /var/lib/mysql/.
# Read the manual for more InnoDB related options. There are many!
# Most important is to give InnoDB 80 % of the system RAM for buffer use:
# https://mariadb.com/kb/en/innodb-system-variables/#innodb_buffer_pool_size
#innodb_buffer_pool_size = 8G

#
# * Galera-related settings
#
# See the examples of server wsrep.cnf files in /usr/share/mariadb
# and read more at https://mariadb.com/kb/en/galera-cluster/

[galera]
# Mandatory settings
#wsrep_on                 = ON
#wsrep_cluster_name       = "MariaDB Galera Cluster"
#wsrep_cluster_address    = gcomm://
#binlog_format            = row
#default_storage_engine   = InnoDB
#innodb_autoinc_lock_mode = 2

# Allow server to accept connections on all interfaces.
#bind-address = 0.0.0.0

# Optional settings
#wsrep_slave_threads = 1
#innodb_flush_log_at_trx_commit = 0
```