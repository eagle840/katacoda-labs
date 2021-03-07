# setup all into a docker container

Dockerfile

'''
FROM ubuntu:20.04
RUN apt --version
RUN apt-get update
RUN apt-get install -y curl
RUN curl -fsSL https://code-server.dev/install.sh | sh
EXPOSE 8080
CMD code-server
'''

`docker build -t coder .`{{execute}}

`docker run -d --name=vsc -p 8080:8080  coder`{{execute}}

