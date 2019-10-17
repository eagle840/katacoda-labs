step a ldap containeer

using the [ldap account manager](https://www.ldap-account-manager.org/lamcms/)

lets check the docker version and make sure it's working

`docker version`{{execute}}

we'll be using the ldap lam, so lets pull the image, from:
[https://hub.docker.com/r/ldapaccountmanager/lam](https://hub.docker.com/r/ldapaccountmanager/lam)

`docker pull ldapaccountmanager/lam`{{execute}}

run start the container
'docker run -p 8080:80 -it -d ldapaccountmanager/lam:stable'{{execute}}

Confirm it's up and running
`curl localhost:8080`{{excute}}

lets connect
https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/

