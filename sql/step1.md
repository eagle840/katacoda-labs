#  Setup and create a simple DB


Lets jump over to docker hub and search for an mysql mage https://hub.docker.com/
You should end up here: https://hub.docker.com/_/mysql

Looking through the notes you'll see  how to startup mysql, 

`docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=1234 -d mysql`{{execute}}

It'll take a minute to pull the image, so wait until you see a container up and running with

`docker ps`{{execute}}  

## Connect to mySQL

`docker exec -it  some-mysql mysql -uroot -p1234`{{execute}} 

-uroot   => user root  
-p       => prompt for password, or -p1234

# create a db

`show databases;`{{execute}}

`create database test1;`{{execute}}

`show databases;`{{execute}}


and exit mysql/container

`exit;`{{execute}} 

(need some help on sql? try: https://www.w3schools.com/sql/default.asp)   

lets stop and remove the container

`docker stop some-mysql`{{execute}}

`docker rm some-mysql `{{execute}}

and start it so  the database is preserved on a local volume  
`mkdir data`{{execute}}
  
`docker run --name some-mysql -v /root/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=1234 -d mysql`{{execute}}

and connect to the container:

`docker exec -it  some-mysql mysql -uroot -p1234`{{execute}}   

``create database test1;`{{execute}}

## Create  a couple of simple tables.

`use test1;`{{execute}}

'
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);'

`SELECT * FROM Customers;`{{execute}}

and now exit and deletel the container:

`exit;`{{execute}}

`docker stop some-mysql`{{execute}}

`docker rm some-mysql `{{execute}}

If you take a look in the data folder you'll see the files created my mysql

`ls data`{{execute}}

