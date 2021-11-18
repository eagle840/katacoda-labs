# setup

`git clone https://github.com/SonarSource/docker-sonarqube.git`{{execute}}

`cd docker-sonarqube/cd docker-sonarqube/cd docker-sonarqube/`{{execute}}

comfirm docker can pull

This fixes a docker problem closing down the sonarcube container:   
`sysctl -w vm.max_map_count=262144`{{execute}}


`docker-compose up -d`{{execute}}

connect to 9000 web page

un and password is admin