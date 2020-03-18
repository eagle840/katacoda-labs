#  Setup and create a simple DB

## Update


## Docker

Lets jump over to docker hub and search for an mysql mage https://hub.docker.com/
You should end up here: https://hub.docker.com/_/mysql

Looking through the notes you'll see  
`docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=1234 -d mysql`{{execute}}

It'll take a minute to pull the image, so wait until you see a container up and running with

`docker ps`{{execute}}  




## Connect to mySQL

`docker run -it --rm mysql mysql -uroot -p`{{execute}} 

-uroot   => user root  
-p       => prompt for password, or -p1234




## Create  a couple of simple tables.