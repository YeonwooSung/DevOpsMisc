# MySQL

[MySQL](https://www.mysql.com/) is an open-source relational database management system (RDBMS).

## Restore DB

There are several ways to restore the MySQL DB.
In general, people use either `mysqldump` with `mysqlbinlog` or `XtraBackup` for restoring the DB.

If the size of the data is not too big, then using the `mysqldump` is a good option.
However, if the size of the DB is too big (i.e. > 10GB) then using the `XtraBackup` is a better option.

For the large DB, mysqldump takes too much time to restore the DB.
Long time restoring could cause the replication delay, and it could lead to the data loss.
Also, in the view of the service subscriber, long unavailable time makes them feel uncomfortable and do not want to keep subscribing the service.

### Use mysqlbinlog for restoring data

The MySQL uses the binary log to record the changes of the database.

The binary log is generally used for backup and replication: the binary log contains a record of all changes to the database data (Disk level) as well as how long each statement took to execute (for performance testing).
When replicating the DB, the slave receives a copy of the binary log from the master and replays the statements recorded in it.

Here, we could realise that the binary log contains all the changes of the database data, so we could use it to restore the data.
As it's name depicts, the binary log is a binary file, so we need to use the `mysqlbinlog` command to convert the binary data into readable texts.

```sh
$ mysqlbinlog 
    --start-datetime="2023-04-27 06:00:00" 
    --stop-datetime="2023-04-27 15:00:00" 
    mysql-bin.000541 > restore.log
$ mysqlbinlog 
    --start-datetime="2023-04-27 06:00:00" 
    --stop-datetime="2023-04-27 15:00:00" 
    mysql-bin.000542 >> restore.log

# 
# Modify restore.log to restore the data
# 

$ mysql -u root -p... [dbname] < restore.log
```

### Use XtraBackup for restoring data

[Percona XtraBackup](https://www.percona.com/software/mysql-database/percona-xtrabackup) is an open-source hot backup utility for MySQL - based servers that doesn't lock your database during the backup.

The XtraBackup supports the following backup types: full backups, incremental backups, partial backups (dbs, tables), compressed (qpress) backups, encrypted backups, etc.

First, create a backup (or replication) user for XtraBackup:

```sql
mysql> CREATE USER 'bkpuser'@'localhost' IDENTIFIED BY 'bkpuser';
mysql> GRANT RELOAD, LOCK TABLES, PROCESS,
       REPLICATION CLIENT ON *.* TO 'bkpuser'@'localhost'; 

mysql> CREATE USER 'repl_user'@'%' IDENTIFIED BY 'repl_user';
mysql> GRANT REPLICATION SLAVE,
       REPLICATION CLIENT ON *.* to 'repl_user'@'%';

mysql> FLUSH PRIVILEGES;
```

Then, create a directory for backup, and run the XtraBackup to get a backup:

```bash
$ sudo mkdir -p /root/backup/

$ sudo xtrabackup \
--defaults-file=/etc/my.cnf \
--host="localhost" \
--user="bkpuser" \
--password="bkpuser" \
--compress \
--compress_threads=4 \
--parallel=4 --no-lock \
--stream=xbstream /tmp > /root/backup/backup.xbstream

# Alternatively, you could use innobackupex to get a backup
$ innobackupex --defaults-file=/etc/my.cnf \
--no-lock \
--user=$ \
--password=$ /root/backup/

# The innobackupex also supports the streaming option with pigz for decompression
$ yum install pigz
$ innobackupex --defaults-file=/etc/my.cnf \
--no-lock \
--user=$ \
--password=$ \
--stream=tar $ | pigz -p $ $/$
```

After getting a backup, you could restore the data with the following steps:

```bash
# Decompress the backup file
$ sudo xtrabackup --decompress /root/backup/

# Prepare the backup
$ sudo xtrabackup --prepare --target-dir=/root/backup/

# Stop the MySQL service
$ sudo systemctl stop mysqld

# Remove the data directory
$ sudo rm -rf /var/lib/mysql/*

# Copy the backup to the data directory
# You could use either copy-back option or move-back option
$ sudo xtrabackup --defaults-file=/etc/my.cnf \
--copy-back \
--target_dir=/root/backup

# Change the permission to prevent "rm -rf" or other commands
$ cd /var/lib
$ sudo chown -R mysql:mysql /var/lib/mysql
$ sudo chmod -R 700 /var/lib/mysql

# Start the MySQL service
$ sudo systemctl start mysqld
```

## References

[1] Woowahan Tech Blog, [장애와 관련된 XtraBackup 적용기](https://techblog.woowahan.com/2576/)
[2] [MySQL Xtrabackup 을 이용한 replication 구성 - 복제 구성](https://hoing.io/archives/15274)
