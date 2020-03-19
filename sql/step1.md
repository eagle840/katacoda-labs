#  Setup and create a simple DB


Lets jump over to docker hub and search for an mysql mage https://hub.docker.com/
You should end up here: https://hub.docker.com/_/mysql

Looking through the notes you'll see  how to startup mysql, 

`docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=1234 -d mysql`{{execute}}

It'll take a minute to pull the image, so wait until you see a container up and running with

`docker ps`{{execute}}  

## Connect to mySQL

`docker exec -it  some-mysql mysql -uroot -p`{{execute}} 

-uroot   => user root  
-p       => prompt for password, or -p1234

# create a db

`show databases;`{{execute}}

`create database test1;`{{execute}}

`show databases;`{{execute}}

and exit mysql/container

`exit`{{execute}}

lets stop and remove the container

`docker stop some-mysql`{{execute}}

`docker rm some-mysql `{{execute}}

and start it so  the database is preserves on a local volume  
`mkdir data`{{execute}}
  
`docker run --name some-mysql -v /root/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=1234 -d mysql`{{execute}}



## Create  a couple of simple tables.





## configs  (start 14:28)


### option 1

mount vol

### option 2

new custom image

lets stop and remove the container ready for the next step.

`docker stop some-mysql`{{execute}}

`docker rm some-mysql `{{execute}}

