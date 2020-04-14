Now we need to create a profile in the account manager:

connect to the service:  
lets connect
https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/


In the ui, on the top right click LAM configuration, and goto general settingx, pw is lam

and set ldaps to the IP address you got from the perivous step, and turn off encryption.

WIP remove:  
# Master password can be found here:
# 
# `docker exec ldap-manager cat config.cfg`{{execute}}

WIP above password is not working is it 'lam'?
docker exec ldap-manager cat  /usr/share/ldap-account-manager/config/lam.conf

Hit OK and you';ll be returned to the LAM login  
You should see the LDAP server IP address.

WIP
see https://github.com/osixia/docker-openldap  
to set password