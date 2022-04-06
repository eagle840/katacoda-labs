# setup

## Git server#
#
follow https://hub.docker.com/r/jkarlos/git-server-docker/

You'll have to do a 

`ssh-keygen -t rsa`{{execute}}

`docker run -d -p 2222:22 --name gitserve -v ~/git-server/keys:/git-server/keys -v ~/git-server/repos:/git-server/repos jkarlos/git-server-docker`{{execute}}

`cp ~/.ssh/id_rsa.pub ~/git-server/keys`{{execute}}

`docker restart gitserve`{{execute}}


--- this point it testing

`cd myrepo`{{execute}}

`git init --shared=true`{{execute}}

`git add .`{{execute}}

`git commit -m "my first commit"`{{execute}}

`cd ..`{{execute}}

`git clone --bare myrepo myrepo.git`{{execute}}

## Sonarcube

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

## GIT server

`docker run -d -p 2222:22 -v ~/git-server/keys:/git-server/keys -v ~/git-server/repos:/git-server/repos jkarlos/git-server-docker`{{execute}}

`cp ~/.ssh/id_rsa ~/git-server/keys`{{execute}} # Keys need to me made

Now restart that docker container : docker retart <###>

`ssh git@0.0.0.0 -p 2222`{{execute}}