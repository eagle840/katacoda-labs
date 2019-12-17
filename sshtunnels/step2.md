## Local Port Forwarding.

try curl from host 1  for workcomputer
`curl <IP>`

iptables -A OUTPUT -d <ip of node01> -p tcp --dport:80 -j REJECT
WIP: block outgoing port on host01 to 80

check

curl <IP>




We're at work on host 1
try connecting
curl <ip>:3386

damn it, those admin's at work are blocking us!

since 3386 is blocked outgoing from were we are, lets try port 8181 to connect to our ssh server.
Our ssh server will then 'reconnect' to our home server with 3386

`ssh -L 8181:<ip>:3386`  username@homeIP

