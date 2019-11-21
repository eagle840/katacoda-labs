

We're at work on host 1
try connecting
curl <ip>:3386

damn it, those admin's at work are blocking us!

since 3386 is blocked outgoing from were we are, lets try port 8181 to connect to our ssh server.
Our ssh server will then 'reconnect' to our home server with 3386

`ssh -L 8181:<ip>:3386`  username@homeIP

