PICTURE HERE

### AT HOME
We''ll start a nginx http server on host 2, our home server

`docker run   -dp 80:80 nginx`{{execute}}
SEEMS TO MESS UP K8S proxy IPABLES
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
`systemctl status ssh.service`{{execute}}
check `/etc/ssh/sshd_config`
    AllowTcpForwarding yes
    Gateway ports yes


### AT WORK

try curl from host 1  for workcomputer
`curl <IP>`

iptables -A OUTPUT -d <ip of node01> -p tcp --dport:80 -j REJECT
WIP: block outgoing port on host01 to 80

check

curl <IP>