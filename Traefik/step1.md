# Set Traefik


`sudo apt install docker-compose`{{execute}}

`mkdir traefik`{{execute}}
`cd traefik/`{{execute}}

(create docker-compose yaml)

'''
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


`sudo docker-compose up -d`{{execute}}

(set password for traefik)
(add port 8080 for traefix admin)