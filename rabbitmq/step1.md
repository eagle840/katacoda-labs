
# run rabbitmq on docker 


We'll be using the rabbitmq container with the management feature installed.

https://hub.docker.com/_/rabbitmq

`docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 rabbitmq:3-management`{{execute}}

`docker ps`{{execute}}

docker exec some-rabbit cat /etc/rabbitmq/rabbitmq.conf

and head over to port 8080 and login  un:guest pw:guest

https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com

