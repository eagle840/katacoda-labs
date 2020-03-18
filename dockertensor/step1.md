
# spin up tensorflow and juypter

 `docker pull tensorflow/tensorflow:latest-py3  # Download latest stable image`{{execute}}

 `docker run -it -p 8888:8888 tensorflow/tensorflow:latest-py3-jupyter  # Start Jupyter server`{{execute}}

 copy the token from the output to connect to the webserver

 or directly print the token

`docker exec -it $(docker ps --format '{{json .}}' | jq -r .ID) cat /root/.local/share/jupyter/runtime/notebook_cookie_secret`{{execute}}
 
 connect to port 8888

 https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com

 and you're ready to go

 