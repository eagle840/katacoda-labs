# Setup

## Overview of SSH tunneling


PICTURE HERE

WIP: Add second tab to bottom terminal
WIP: master will be 'HOME'
### AT HOME
We''ll start a nginx http server on host 2, our home server

`docker run   -dp 80:80 -net host -v /opt/html:/opt/html nginx`{{execute}}
SEEMS TO MESS UP K8S proxy IPABLES on node01, RUN on master, but add tab on node01
k run http --image=nginx
k expose deploy/http --port 80 --external-ip <ip of node01>


check its working (on node01)

`curl localhost`{{execute}}
and we should get back some html

check nginx is listening on 80
`netstat -tal`{{execute}}

lets get ip (with direct connection to internet, or forward 22 to your PC from your router/firewall)
`ip addr`{{execute}}


### CHECK SSH SERVER
make sure ssh server is running
`system status | grep -i ssh`{{execute}}

It appears ssh is running as ssh.service

`systemctl status ssh.service`{{execute}}

check `/etc/ssh/sshd_config` to make sure setting are correct
    AllowTcpForwarding yes
    Gateway ports yes


