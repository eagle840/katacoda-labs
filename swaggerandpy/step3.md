


## create docker


WIP add vol to get titanic file into docker   

WIP mysql doesn't allow `load data` by default, so we have to use an updated my.cnf in the docker image.


echo '[mysqld]' >> /etc/mysql/my.cnf

echo local-infile >> /etc/mysql/my.cnf

echo '[mysql]' >> /etc/mysql/my.cnf

echo local-infile >> /etc/mysql/my.cnf

## creat docker file:

dockerfile:

```
FROM mysql
COPY my.cnf /etc/mysql/my.cnf
```

`docker build -t my_docker:v1 .`{{execute}}



docker cp into container:/etc/mysql/my.cnf




WIP docker restart my_mysql ?  > docker restart [id|name]

`docker run --name my_mysql -v titantic.csc:/ -e MYSQL_ROOT_PASSWORD=password -d mysql`

### connect to mysql

`docker exec -it my_mysql bash`
root@ce2a9451906e:/# mysql -p
Enter password:

### create database

status


show databases;

create database titanic;

use titanic;


### create table

```
create table passengers (
     uuid int unsigned not null auto_increment,
     Survived binary not null,
     Pclass  tinyint not null,
     Name  varchar(50) not null,
     Sex varchar(10) not null,
     Age tinyint not null,
     S_Aboard tinyint not null,
     P_Aboard tinyint not null,
     Fare   decimal not null,
     primary key (uuid),
     key name (name)
     )engine=innodb
     default charset=utf8;```{{copy}}

### load titantic database

https://medium.com/@AviGoom/how-to-import-a-csv-file-into-a-mysql-database-ef8860878a68

LOAD DATA LOCAL INFILE '/Users/miguelgomez/Desktop/mock_data.csv' INTO TABLE users FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id, first_name, last_name, email, transactions, @account_creation)SET account_creation  = STR_TO_DATE(@account_creation, '%m/%d/%y');

offical ref: https://dev.mysql.com/doc/refman/8.0/en/load-data.html


LOAD DATA LOCAL INFILE '/titanic.csv' INTO TABLE passengers FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (Survived,Pclass,Name,Sex,Age,S_Aboard,P_Aboard,Fare);

WIP getting error:
ERROR 3948 (42000): Loading local data is disabled; this must be enabled on both the client and server sides
WIP ^^^^ Fixed
https://stackoverflow.com/questions/10762239/mysql-enable-load-data-local-infile


WIP survived col is not correct,  containes 0x30
WIP: possible fix:

LOAD DATA LOCAL INFILE '/titanic.csv' INTO TABLE passengers FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (@Survived,Pclass,Name,Sex,Age,S_Aboard,P_Aboard,Fare)  SET Survived = UNHEX(@Survived) ;

taken from (need to confirm results):
https://stackoverflow.com/questions/12038814/import-hex-binary-data-into-mysql




WIPL noted that a uuid is not included in the table
WIP   the listing of the headers or the db column fields?