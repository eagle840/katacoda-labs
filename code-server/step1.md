

# IN PROGRESS

`sudo apt update`{{execute}}

`curl -fsSL https://code-server.dev/install.sh | sh`{{execute}}

review docs  https://github.com/cdr/code-server/blob/v3.9.0/docs/guide.md

'code-server' will start, but only on local host, lets expose it on the internet so you can access it.

`code-server --bind-addr 0.0.0.0:8080 &`{{execute}}


To connect

https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com


The password is stored in ~/.config/code-server/config.yam, we'll pull it from a second terminal window

`cat .config/code-server/config.yaml`{{execute t2}}


