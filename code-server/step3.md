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

`docker run -d --name=vsc -p 8080:8080  coder`{{execute}}

Note that the password in outputed when you run `docker run`

