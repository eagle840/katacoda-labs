# setup

`git clone https://github.com/SonarSource/docker-sonarqube.git`{{execute}}

`cd docker-sonarqube/example-compose-files/sq-with-postgres/`{{execute}}

comfirm docker can pull

This fixes a docker problem closing down the sonarcube container:   
`sysctl -w vm.max_map_count=262144`{{execute}}


`docker-compose up -d`{{execute}}

confirm both containers are up:   
`docker-compose ps`{{execute}}

connect to 9000 web page   
https://[[HOST_SUBDOMAIN]]-9000-[[KATACODA_HOST]].environments.katacoda.com

un and password is admin