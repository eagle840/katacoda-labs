# Setup a keycloak server with docker

`docker run  -p 8080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=pass jboss/keycloak`{{execute}}

connect to the server by clicking on the keycloak tab

https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com

click on the admin console

and login with  `user: admin` & `password:pass`

WIP:
admin login page is loading, but browser refusing to load 'unsafe script'
when allowing 'unsafe script' getting the following message on the page
We are sorry...
Invalid parameter: redirect_uri

« Back to Application

Possible Troubleshoot resource @
https://stackoverflow.com/questions/45352880/keycloak-invalid-parameter-redirect-uri/50776053

https://hub.docker.com/r/jboss/keycloak

run on isolated server on test setup