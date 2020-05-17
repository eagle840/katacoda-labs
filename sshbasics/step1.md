the system has been setup and logined in with root

alexissetup alexis

`useradd -m -c "comment for alexis" -s /bin/bash alexis`{{execute}}

password change for current user is

'passwd'

passwd <username>  will change that users password

`passwd alexis`{{execute}}

and enter a password 1234

login to alexis
su alexis    

try and do a sudo apt update 
it fails

go back to root   (or admin if setup)   
exit

run    visudo      (@6:50)




