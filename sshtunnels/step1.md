# Setup

## Overview of SSH tunneling


PICTURE HERE
![alt text](https://upload.wikimedia.org/wikipedia/commons/d/dc/Ssh-L-Tunnel.png "Logo Title Text 1")

![alt text](https://upload.wikimedia.org/wikipedia/commons/2/2c/SSH_Tunnel_%28remote%29.png "Logo Title Text 1")

### AT HOME (host01)
We'll start a nginx http server on host 1, our home server

`docker run   -dp 80:80 --network host -v /opt/html:/opt/html nginx`{{execute}}

check its working (on node01)

`curl localhost`{{execute}}
and we should get back some html



### CHECK SSH SERVER
Lets see if a ssh service is running on this machine.
`systemctl status | grep -i ssh`{{execute}}

It appears ssh is running as ssh.service

`systemctl status ssh.service`{{execute}}

check `/etc/ssh/sshd_config` to make sure setting are correct
    AllowTcpForwarding yes
    Gateway ports yes

`cat /etc/ssh/sshd_config`{{execute}}


