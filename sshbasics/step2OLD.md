Lets connect to node01 (as root)   
`ssh node01`{{execute}}   

And make a new user:   
`useradd -m -c "this is userx" -s /bin/bash userx`{{execute}}   
   
`passwd userx`{{execute}}

And return to master.   
`exit`{{execute}}  
Lets try connecting with a password:   
`ssh userx@node01`{{execute}}     

so this shows I can ssh from the same network


`curl diagnostic.opendns.com/myip`{{execute}}

open putty and try to connect  > error

create ssh keys and try to connect


Generate your key
`ssh-keygen`
Configure ssh to use the key
`vim ~/.ssh/config`   

Host SERVERNAME
Hostname ip-or-domain-of-server
User USERNAME
PubKeyAuthentication yes
IdentityFile ./path/to/key


Copy your key to your server
`ssh-copy-id -i /path/to/key.pub SERVERNAME`
