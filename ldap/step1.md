## step a openLDAP  container

using the [ldap account manager](https://www.ldap-account-manager.org/lamcms/)

lets check the docker version and make sure it's working

`docker version`{{execute}}


lets use the docker container provided by [https://github.com/osixia/docker-openldap](https://github.com/osixia/docker-openldap) 

`docker run -p 389:389 -p 636:636 --name my-openldap-container --detach osixia/openldap:1.3.0`{{execute}}

Note that it's using the standard ports for LDAP; 389 and secure 636

lets confirm it's working by running a ldapseach query against it
`docker exec my-openldap-container ldapsearch -x -H ldap://localhost -b dc=example,dc=org -D "cn=admin,dc=example,dc=org" -w admin`{{execute}}

and take a look at the startup log
`docker logs my-openldap-container`{{execute}}

and moke a note of the ip of the 'my-openldap-container' - jq will prettyify the output
`docker network inspect bridge | jq`{{execute}}