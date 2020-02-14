


## create docker




WIP add vol to get titanic file into docker   
docker run --name my_mysql \
>  -e MYSQL_ROOT_PASSWORD=password \
> -d \
> mysql

### connect to mysql

$ docker exec -it my_mysql bash
root@ce2a9451906e:/# mysql -p
Enter password:

### create database

show databases;

create database titantic;

use titantic;


### create table

create table passengers (
    -> uuid int unsigned not null auto_increment,
    -> Survived binary not null,
    -> Pclass  tinyint not null,
    -> Name  varchar(50) not null,
    -> Sex varchar(10) not null,
    -> Age tinyint not null,
    -> S_Aboard tinyint not null,
    -> P_Aboard tinyint not null,
    -> Fare   decimal not null,
    -> primary key (id),
    -> key name (name)
    -> )engine=innodb
    -> default charset=utf8;

### locad titantic database

https://medium.com/@AviGoom/how-to-import-a-csv-file-into-a-mysql-database-ef8860878a68

LOAD DATA LOCAL INFILE '/Users/miguelgomez/Desktop/mock_data.csv' INTO TABLE users FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id, first_name, last_name, email, transactions, @account_creation)SET account_creation  = STR_TO_DATE(@account_creation, '%m/%d/%y');

offical ref: https://dev.mysql.com/doc/refman/8.0/en/load-data.html


LOAD DATA LOCAL INFILE '/titanic.csv' INTO TABLE passengers FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare);

WIPL noted that a uuid is not included in the table
WIP   the listing of the headers or the db column fields?