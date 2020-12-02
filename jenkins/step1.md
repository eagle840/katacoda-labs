# Setup files/folders

Let's first setup a folder to store our Jenkins data:   

`mkdir jenkins`{{execute}}

`chmod 777 jenkins`{{execute}}

and pull the Jenkin's Image:   

`docker pull jenkins/jenkins:2.255`{{execute}}     
[WIP try pulling  jenkins/jenkins:lts  # change the one in step 3 if ness   
`docker pull mailhog/mailhog`{{execute}}   

`nano docker-compose.yml`{{execute}}

```yaml
version: "3.8"

services:

  jenkins:
    image: jenkins/jenkins:2.255
    ports:
    - "8080:8080"
    volumes:
    - ./jenkins:/var/jenkins_home
    restart: unless-stopped

  mails:
    image: mailhog/mailhog
    restart: unless-stopped
    ports:
    - "8025:8025"
```

# start the jenkins docker container

`docker-compose up`{{execute}}

when jenkins comes up, you'll see the password in stdout

OR

`docker exec root_jenkins_1 cat /var/jenkins_home/secrets/initialAdminPassword`{{execute}}


open pages  for  8025  and 8080  

https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com

https://[[HOST_SUBDOMAIN]]-8025-[[KATACODA_HOST]].environments.katacoda.com

# configure access to port 2375

lets check the status of the docker service

`sudo systemctl status docker.service`{{execute}}

lets open up port 2375 so we can allow jenkins to interact with the docker daemon data

`sudo nano /lib/systemd/system/docker.service`{{execute}}   

find the line: starting with  ExecStart in the [service] and add `-H tcp://0.0.0.0` just after  fd://

and restart the docker daemon

`sudo systemctl daemon-reload`{{execute}}
`sudo systemctl restart docker.service`{{execute}}

and make sure we're getting the json data



`curl localhost:2375/containers/json | jq`{{execute}}
