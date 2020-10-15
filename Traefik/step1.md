# Set Traefik


`sudo apt install docker-compose -y`{{execute}}

Confirm  asuccessful install:    
`docker-compose version`{{execute}}

`mkdir traefik`{{execute}}
`cd traefik/`{{execute}}

Create the docker-compose file:
`nano docker-compose.yaml`{{execute}}   


'''yaml
version: '3'

services:
  reverse-proxy:
    # The official v2 Traefik docker image
    image: traefik:v2.3
    # Enables the web UI and tells Traefik to listen to docker
    command: --api.insecure=true --providers.docker
    ports:
      # The HTTP port
      - "80:80"
      # The Web UI (enabled by --api.insecure=true)
      - "8080:8080"
    volumes:
      # So that Traefik can listen to the Docker events
      - /var/run/docker.sock:/var/run/docker.sock
'''

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

`curl localhoat`{{execute}}   

note that you'll get a `404 page not found` - this is Traefik telling you that port 80 hasn't been setup


WIP: port 8080 isn't coming up - ?turn off the secure api?
     check out  https://doc.traefik.io/traefik/getting-started/quick-start/