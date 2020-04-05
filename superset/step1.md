# Setup requirements

#### update docker and docker-compose

`apt upgrade docker.io`{{execute}}

`pip install --upgrade pip`{{execute}}

Docker-compose is not upto date in apt, so remove and manually install the latest version

`apt-get remove docker-compose`{{execute}}

`sudo rm /usr/local/bin/docker-compose`{{execute}}

`pip uninstall docker-compose`{{execute}}

Install instructions can be found at https://docs.docker.com/compose/install/

`sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`

`sudo chmod +x /usr/local/bin/docker-compose`{{execute}}

and lets start docker-compose

** WIP needs 3GB? **

`docker-compose up`{{execute}}