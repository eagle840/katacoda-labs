PICTURE HERE

We''ll start a nginx http server on host 2, our home server

`docker run -dp 80:3386 nginx`

check its working

curl localhost:3386

check nginx is listening on 80
`netstat -tl`

get ip
`ip addr`

make sure ssh server is running
systemctl status ssh.service
check /etc/ssh/sshd.config
   AllowTcpForwarding yes
    Gateway ports yes


try curl from host 1  for workcomputer
curl <IP>:3386

block outgoing port on host01 to 80

check

curl <IP>