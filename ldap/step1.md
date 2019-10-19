step a ldap containeer

using the [ldap account manager](https://www.ldap-account-manager.org/lamcms/)

lets check the docker version and make sure it's working

`docker version`{{execute}}


lets use [https://github.com/osixia/docker-openldap](https://github.com/osixia/docker-openldap) docker image

`docker run -p 389:389 -p 636:636 --name my-openldap-container --detach osixia/openldap:1.3.0`{{execute}}


lets confirm it's working
`docker exec my-openldap-container ldapsearch -x -H ldap://localhost -b dc=example,dc=org -D "cn=admin,dc=example,dc=org" -w admin`{{execute}}

and take a look at the startup log
`docker logs my-openldap-container`{{execute}}

and moke a note of the ip  - jq will prettyify the output
`docker network inspect bridge | jq`{{execute}}