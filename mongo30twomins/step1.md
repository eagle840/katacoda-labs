# Setup a Mongo DB server and admin



### Create your docker compose file

In this lab we'll be useing the docker images mongo and mongo-express


`mkdir compose1 && cd compose1`{{execute}}

`nano docker-compose.yml`{{execute}}

Cut and paste (ctrl-inst, shft-inst) in the following then save and exit  (ctrl-o then ctrl-x)

```
# Use root/example as user/password credentials
version: '3.1'

services:

  mongo:
    image: mongo
    restart: always
    ports:
      - 27017:27017
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

bring the containers up:

`docker-compose up -d`{{execute}}

check they are up

`docker-compose ps`{{execute}}

Lets connect to the server itself:

you can connect to the container in either way:  

`docker exec -it compose1_mongo_1 /bin/bash`{{execute}}

OR

`docker-compose exec mongo /bin/bash`{{execute}}

lets check the version we're running:

`mongo --version`{{execute}}

You can enter the Mongo shell with:   
  `mongo -uroot -pexample`   
the help command is `help` and to exit `exit`

If you'd like to discover more about mongo shell try: https://docs.mongodb.com/manual/tutorial/access-mongo-shell-help/

When  finished with the shell exit the container:      
`exit`{{execute}}

### Connect to the web admin portal

Lets connect to the web admin:

https://[[HOST_SUBDOMAIN]]-8081-[[KATACODA_HOST]].environments.katacoda.com

And that's it you're done. Feel free to play around with the admin console,

OR

start up a mongo console,

`docker-compose exec mongo mongo`{{execute}}

 and follow along with [Mongo's getting started](https://docs.mongodb.com/manual/tutorial/getting-started/)





