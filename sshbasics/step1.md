the system has been setup and logined in with root


lets create an admin account
useradd -m -c "comment for alexis" -s /bin/bash admin
 SEE VIDEO FOR SUDO SETUP


lets change sudo for admin



setup alexis

useradd -m -c "comment for alexis" -s /bin/bash alexis


password change for current user is

passwd

passwd <username>  will change that users password

login to alexis
su alexis    

try and do a sudo apt update 
it fails

go back to root   (or admin if setup)   
exit

run    visudo      (@6:50)




