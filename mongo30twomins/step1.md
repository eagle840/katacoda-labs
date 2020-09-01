# Setup a Mongo DB server and web admin in under 2 minutes

# Create your docker compose file

In this lab we'll be useing the docker images mongo and mongo-express


`mkdir compose1 && cd compse1`{{execute}}

`nano docker-compose.yml`{{execute}}

paste in the following and save  (ctrl-x then ctrl-s)

```
# Use root/example as user/password credentials
version: '3.1'

services:

  mongo:
    image: mongo
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example

  mongo-express:
    image: mongo-express
    restart: always
    ports:
      - 8081:8081
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: example

```

bring the container up:

`docker-compose up -d`{{execute}}

check they are up

`docker-compose ps`{{execute}}

connect to the web admin:

https://[[HOST_SUBDOMAIN]]-8081-[[KATACODA_HOST]].environments.katacoda.com


