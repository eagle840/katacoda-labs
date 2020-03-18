# Save And Restore


## Save

store mysql root password in /root/.my.cnf   (chmod 600 .my.cnf)

[client]
user=root
password=1234


### backup one db

mysqldump --add-drop-table --database <name>  > ~/backups/db/$(/bin/date '+\%Y-%m-\%d').sql.bak

* pw pulled from .my.cnf

### backup all

mysqldump --all-databases --all-routines > ~/backups/allbds/fulldump.sql

## Restore

mysql -uroot -p [database name] < <backupname>.sql

mysql -uroot -p < fulldump.sql



## Reset password

from: stackoverflow.com/questions/11657829/error-2002-hy000-cant-connect-to-local-mysql-server-through-socket-var-run

Stop mysql

sudo /etc/init.d/mysql stop
Or for other distribution versions:

sudo /etc/init.d/mysqld stop
Start MySQL in safe mode

sudo mysqld_safe --skip-grant-tables &
Log into MySQL using root

mysql -uroot
Select the MySQL database to use

use mysql;
Reset the password

-- MySQL version < 5.7
update user set password=PASSWORD("mynewpassword") where User='root';

-- MySQL 5.7, mysql.user table "password" field -> "authentication_string"

update user set authentication_string=password('mynewpassword') where user='root';
Flush the privileges

flush privileges;
Restart the server

quit
Stop and start the server again

Ubuntu and Debian:

sudo /etc/init.d/mysql stop
...
sudo /etc/init.d/mysql start
On CentOS, Fedora, and RHEL:

sudo /etc/init.d/mysqld stop
...
sudo /etc/init.d/mysqld start
Login with a new password

mysql -u root -p