# Setup files/folders

`mkdir jenkins`{{execute}}
`chmod www jenkins`{{execute}}

nano docker-compose.yml

'''yaml
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
'''

`docker-compose up`{{execute}}