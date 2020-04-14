setup ldap lam

We'll be using the ldap lam, so lets pull the image, from:
[https://hub.docker.com/r/ldapaccountmanager/lam](https://hub.docker.com/r/ldapaccountmanager/lam)

It's webite is: https://www.ldap-account-manager.org/lamcms/shop

configuration files are in:
- /etc/ldap-account-manager
- /var/iib/ldap-account-manager

run start the container
`docker run -p 8080:80 --name ldap-manager -it -d ldapaccountmanager/lam:stable`{{execute}}

make sure the container is running
`docker ps`{{execute}}

Confirm it's up and running  
`curl localhost:8080`{{execute}}

