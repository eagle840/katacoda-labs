# Setup files/folders

`mkdir jenkins`{{execute}}
`chmod 777 jenkins`{{execute}}

`docker pull jenkins/jenkins:2.255`{{execute}}
`docker pull mailhog/mailhog`{{execute}}

`nano docker-compose.yml`{{execute}}

```yaml
version: "3.8"

services:

  jenkins:
    image: jenkins/jenkins:2.255
    ports:
    - "9080:8080"
    volumes:
    - ./jenkins:/var/jenkins_home
    restart: unless-stopped

  mails:
    image: mailhog/mailhog
    restart: unless-stopped
    ports:
    - "8025:8025"
```

`docker-compose up`{{execute}}

when jenkins comes up, you'll see the password in stdout

OR

`docker exec root_jenkins_1 cat /var/jenkins_home/secrets/initialAdminPassword`{{execute}}


open pages  for  8025  and 9080  (also 50000 is open for jenkins agents)