
# Generate a database

In this step we'll generate a database from a csv file to serve as the backend. (titantic.csv)

Off course the easir way is to just use a csv to sql converter like:

https://codebeautify.org/csv-to-sql-converter#

## create docker

Lets pull the mysql image

`docker pull mysql`{{execute}}

and start it 

`docker run --name my_mysql -v $PWD/titanic.csv:/ -e MYSQL_ROOT_PASSWORD=password -d mysql`{{execute}}

Out of the box mysql will not allow to load in data (LOAD DATA), so we need to make some adjustments to my.conf

we need the /etc/mysql/my.cnf   file to advise it to allow loading external data

`docker cp my_mysql:/etc/mysql/my.cnf .`{{execute}}
 
we'll add the config items to allow 'LOAD DATA'

`echo '[mysqld]' >> my.cnf`{{execute}}

`echo local-infile >> my.cnf`{{execute}}

`echo '[mysql]' >> my.cnf`{{execute}}

`echo local-infile >> my.cnf`{{execute}}

and copy it back into the container

`docker cp my.cnf my_mysql:/etc/mysql/ `{{execute}}

and lets restart the docker container to apply the changes

`docker restart my_mysql`{{execute}}

### connect to mysql

`docker exec -it my_mysql bash`{{execute}}  

Lets make sure the titanic file copied across:

`ls`{{execute}}

`mysql -p`{{execute}}

enter the password: 'password'

### create database

`status;`{{execute}}

Note that the 'current database' is blank

`show databases;`{{execute}}

`create database titanic;`{{execute}}

`use titanic;`{{execute}}


### create table

**should be data types according to swagger yaml**

survived	boolean
passengerClass	integer
name	string
sex	string
Enum:
[ male, female, other ]
age	integer
siblingsOrSpousesAboard	integer
parentsOrChildrenAboard	integer
fare	number
uuid	string($uuid)

```
create table passengers (
     uuid int unsigned not null auto_increment,
     Survived bool not null, 
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
     default charset=utf8;
     
```{{copy}}

Note (in linux copy/paste is ctrl-insert/shift-insert)

and check it

`describe passengers;`{{execute}}

### load titantic database


```
LOAD DATA LOCAL INFILE '/titanic.csv' INTO TABLE passengers FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (@Survived,Pclass,Name,Sex,Age,S_Aboard,P_Aboard,Fare)  SET Survived = UNHEX(@Survived) ;
```{{copy}}

*WIP* survived is NOT boolean, using boolean is datatype results in all 0's

can lets check the table entries:

`SELECT * FROM passengers LIMIT 10;`{{execute}}



WIPL noted that a uuid is not included in the table
WIP   the listing of the headers or the db column fields?




# OLD

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