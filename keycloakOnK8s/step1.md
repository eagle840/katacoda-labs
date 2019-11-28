# Setup a keycloak server with docker

`docker run  -p 8080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=pass jboss/keycloak`{{execute}}

connect to the server by clicking on the keycloak tab

https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com

and login with  `user: admin` & `password:pass`
