# Set Traefik


`sudo apt install docker-compose -y`{{execute}}

Confirm  asuccessful install:    
`docker-compose version`{{execute}}

`mkdir traefik`{{execute}}
`cd traefik/`{{execute}}

Create the docker-compose file:
`nano docker-compose.yaml`{{execute}}   


'''yaml

version: "3.3"

services:

  traefik:
    image: "traefik:v2.5"
    container_name: "traefik"
    command:
      #- "--log.level=DEBUG"
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
    ports:
      - "80:80"
      - "8080:8080"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"

  whoami:
    image: "traefik/whoami"
    container_name: "simple-service"
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.whoami.rule=Host(`whoami.localhost`)"
      - "traefik.http.routers.whoami.entrypoints=web"

'''

pulled from: https://doc.traefik.io/traefik/user-guides/docker-compose/basic-example/

Bring the containers up:   
`sudo docker-compose up -d`{{execute}}   

and confirm:
`sudo docker-compose ps`{{execute}}  

Connect to the dashboard:   
https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com

be sure to set the password within x mins
(set password for traefik)
(add port 8080 for traefix admin)

Lets try and access the stand http port 80

`curl localhost`{{execute}}   

note that you'll get a `404 page not found` - this is Traefik telling you that port 80 hasn't been setup


WIP: port 8080 isn't coming up - ?turn off the secure api?
     check out  https://doc.traefik.io/traefik/getting-started/quick-start/
