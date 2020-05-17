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
