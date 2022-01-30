# setup all into a docker container

Dockerfile


create a Dockerfile and paste in:

```
FROM ubuntu:20.04
RUN apt --version
RUN apt-get update
RUN apt-get install -y curl
RUN curl -fsSL https://code-server.dev/install.sh | sh
EXPOSE 8080
# CMD code-server
CMD ["code-server", "--bind-addr=0.0.0.0:8080"]
```

`docker build -t coder .`{{execute}}

`docker run -d --name=vsc -p 8088:8080  coder`{{execute}}

confirm the doccker container is up:
`docker ps`{{execute}}

To get the password to login

`docker exec vsc cat ~/.config/code-server/config.yaml`{{execute}}

To connect

https://[[HOST_SUBDOMAIN]]-8088-[[KATACODA_HOST]].environments.katacoda.com

