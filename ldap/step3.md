
## setup ldap lam

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

Now we need to create a profile in the account manager:

connect to the service:  
lets connect
https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/


In the ui, on the top right click LAM configuration, and goto general settingx, pw is lam

and set ldaps to the IP address you got from the perivous step, and turn off encryption.

WIP remove:  
 Master password can be found here:
 
 `docker exec ldap-manager cat config.cfg`{{execute}}

WIP above password is not working is it 'lam'?
docker exec ldap-manager cat  /usr/share/ldap-account-manager/config/lam.conf

Hit OK and you';ll be returned to the LAM login  
You should see the LDAP server IP address.

WIP
see https://github.com/osixia/docker-openldap  
to set password