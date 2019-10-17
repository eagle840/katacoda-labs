setup ldap lam

We'll be using the ldap lam, so lets pull the image, from:
[https://hub.docker.com/r/ldapaccountmanager/lam](https://hub.docker.com/r/ldapaccountmanager/lam)

`docker pull ldapaccountmanager/lam`{{execute}}

run start the container
`docker run -p 8080:80 -it -d ldapaccountmanager/lam:stable`{{execute}}

make sure the container is running
`docker ps`{{execute}}

Confirm it's up and running
`curl localhost:8080`{{excute}}

lets connect
https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/