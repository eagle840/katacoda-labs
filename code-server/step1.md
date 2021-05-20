

# IN PROGRESS

`sudo apt update`{{execute}}

`curl -fsSL https://code-server.dev/install.sh | sh`{{execute}}

review docs  https://github.com/cdr/code-server/blob/v3.9.0/docs/guide.md

'code-server' will start, but only on local host, lets expose it on the internet so you can access it.

`code-server --bind-addr 0.0.0.0:8080`{{execute}}

Lets gets the password:

`cat ~/.config/code-server/config.yaml`{{execute t2}

To connect

https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com


The password is stored in ~/.config/code-server/config.yam

`cat .config/code-server/config.yam`{{execute t2}}

# need to

secure with password

use with ssh (as in docs)

add cert - lets encrypt

setup python 

put in a docker container