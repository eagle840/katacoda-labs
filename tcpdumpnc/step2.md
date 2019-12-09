## overview of nc

Netcat (nc) is a utility for reading and righting directly from a network connection (tcp and udp)

Lets see if ssh is running on port 22 on this server, since tcp protocol is the default there is no need to define it. (-u will specify UDP)

`nc localhost 22`{{execute}}

we'll see a responce back from the server `SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3` 

`echo stop`{{ execute }}


### FIX HOST 2 FIRST
Lets setup a simple server on host2 with `-l` for listen and on port 1234 `-p 1234

`nc -l -p 1234`{{execute}}

and connect to it on the other server

`nc host2 123`{{execute host2}}

if you're not getting the output you expect you can use `-v` or `-vv` for verbose output to help trouble shoot.

in fact, lets try connecting to  googles dns service on UDP 53

`nc -u –vv  8.8.8.8 53`{{execute}}

Next up, lets try a little port scanning with `-z`, and this time like tcpdump we'll use `-n` to suppress name resolution. The last argument here specifies the port range 1 to 30

`netcat -z -vv -n 127.0.0.1 1-30`{{execute}}


### resources

(wikipedia with examples)[https://en.wikipedia.org/wiki/Netcat]
(netcat offical site)[http://nc110.sourceforge.net/]
