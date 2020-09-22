The top terminal is this lab we'll consider ther server and the bottom one the client.


# Top termainal (server)

You're presently logged in with root, so lets setup a new user, alexis

`useradd -m -c "comment for alexis" -s /bin/bash alexis`{{execute}}

and set a new password for them:

`passwd alexis`{{execute}}

and enter a password 1234

Take a quick look at the passwd file and you'll see alexis added.
`cat /etc/passwd`{{execute}}

and the group file:
`cat /etc/group`{{execute}}

and the groups command:
`groups alexis`{{execute}}


Lets give some (all) sudo priveleges

`sudo visudo`{{execute}}

and add to  the end of the file:
`alexis ALL=(ALL) NOPASSWD: ALL`

Now login to alexis

`login alexis`{{execute}}

double check who we are

`whoami`{{execute}}

and exit back to the root account.

`exit`{{execute}}

# Setup the bottom terminal (client)


Lets create a slight different user name and login


`useradd -m -c "comment for alex" -s /bin/bash alex`{{execute HOST2}}

and set a new password for them:

`passwd alex`{{execute HOST2}}

and enter a password 4321

Lets give some (all) sudo priveleges

`sudo visudo`{{execute HOST2}}

and add to  the end of the file:
`alex ALL=(ALL) NOPASSWD: ALL`

and login

`login alex`{{execute HOST2}}

Lets generate show ssh keys, with a type of rsa:

`ssh-keygen -t rsa`{{execute HOST2}}

keep the default key location:  `/home/alex/.ssh/id_rsa`

and we'll leave the password blank

Lets take a look at the two files generated:

`ls -lash .ssh`{{execute HOST2}}

The id_rsa is the private key, note how it is marked PRIVATE KEY

`cat .ssh/id_rsa`{{execute HOST2}}

and id_rsa.pub is the public key

`cat .ssh/id_rsa.pub`{{execute HOST2}}

Now let copy the key we generated over to the server:

`ssh-copy-id  alexis@host01`{{execute HOST2}}

enter the password for alexia on the server (1234)

and now we can connect to the server just using the key

`ssh alexis@host01`{{execute HOST2}}



