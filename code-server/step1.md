

# IN PROGRESS

`sudo apt-get updates`{{execute}}

`curl -fsSL https://code-server.dev/install.sh | sh`{{execute}}

review docs  https://github.com/cdr/code-server/blob/v3.9.0/docs/guide.md

'code-server' will start, but only on local host, lets expose it on the internet so you can access it.

`code-server --bind-addr 0.0.0.0:8080`{{execute}}

add link to url

'~/.config/code-server/config.yaml'  in second terminal




# need to

secure with password

use with ssh (as in docs)

add cert - lets encrypt

setup python 

put in a docker container