You're presently logged in with root, so lets setup a new user, alexis

`useradd -m -c "comment for alexis" -s /bin/bash alexis`{{execute}}

and set a new password for them:

`passwd alexis`{{execute}}

and enter a password 1234

Take a quick look at /etc/
location of password file.


and the groups command:


CMD to check GROUPs

Now login to alexis

`login alexis`{{execute}}

double check who we are

`whoami`{{execute}}

and exit back to the root account.

`exit`{{execute}}

Now lets jump over to node01

ssh node02


----------
Lets generate show ssh keys:

`ssh-keygen`

keep the default key location:  `/home/alexis/.ssh/id_rsa`

and we'll leave the password blank

Lets take a look at the two files generated:

`ls -lash .ssh`{{execute}}

The id_rsa is the private key

`cat .ssh/id_rsa`{{execute}}

and id_rsa.pub is the public key

`cat .ssh/id_rsa.pub`{{execute}}

run    visudo      (@6:50)




