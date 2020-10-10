## Local Port Forwarding.

Lets pretend that the top terminal, host01, is your home PC 
and host02 is your work.

try curl from host 2  for workcomputer
`curl host01`{{execute HOST2}}


Let say our boss is a real meany, and blocks out interwebs access'
(we'll block port 80 on host01)

`iptables -A INPUT -p tcp --destination-port 80 -j DROP`{{execute}}


check

`curl host01`{{execute HOST2}}

notice there is no reponse (ctrl-c)


We're at work on host 1
try connecting
curl <ip>:3386

damn it, those admin's at work are blocking us!



since 3386 is blocked outgoing from were we are, lets try port 8181 to connect to our ssh server.
Our ssh server will then 'reconnect' to our home server with 3386

`ssh -L 8181:host01:80  root@host01`{{execute HOST2}}

Lets take a look at the man for ssh -L

``` 
-L \[Bind_address:]port:remote_socket
 
-L local_socket:host:hostport
 
-L local_socket:remote_socket
Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to the given host and port, or Unix socket, on the remote side. This works by allocating a socket to listen to either a TCP port on the local side, optionally bound to the specified bind_address, or to a Unix socket. Whenever a connection is made to the local port or socket, the connection is forwarded over the secure channel, and a connection is made to either host port hostport, or the Unix socket remote_socket, from the remote machine.
Port forwardings can also be specified in the configuration file. Only the superuser can forward privileged ports. IPv6 addresses can be specified by enclosing the address in square brackets.

By default, the local port is bound in accordance with the GatewayPorts setting. However, an explicit bind_address may be used to bind the connection to a specific address. The bind_address of “localhost” indicates that the listening port be bound for local use only, while an empty address or ‘*’ indicates that the port should be available from all interfaces.
```
