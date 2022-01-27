#  setup git server

https://www.linux.com/training-tutorials/how-run-your-own-git-server/

Better still, create it in a docker container

https://hub.docker.com/r/jkarlos/git-server-docker/
#

`docker run -d -p 2222:22 -v ~/git-server/keys:/git-server/keys -v ~/git-server/repos:/git-server/repos jkarlos/git-server-docker`{{exxecute}}

confirm it's running:
`docker ps`{{execute}}
