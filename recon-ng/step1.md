# Recon-ng on Docker


WIP: check https://github.com/lanmaster53/recon-ng/wiki/Getting-Started#using-docker   
and match with what do do below
DO NOT Pull the docker hub image, it is the old version 4

`mkdir .recon-ng`{{execute}}   

We can generate our own docker image, or pull one I've pre-built

`docker run --rm -it -p 5000:5000 -v $(pwd):/recon-ng -v ~/.recon-ng:/root/.recon-ng --entrypoint "./recon-ng" eagle840/recon-ng`{{execute}} 

## OR  (~5 minutes)

Lets pull the repo:
`git clone https://github.com/lanmaster53/recon-ng.git`{{execute}}   

`cd recon-ng`{{execute}}   

and build an image:
`docker build --rm -t recon-ng .`{{execute}}   

and run it:
`docker run --rm -it -p 5000:5000 -v $(pwd):/recon-ng -v ~/.recon-ng:/root/.recon-ng --entrypoint "./recon-ng" recon-ng`{{execute}}   


WIP read the rest of the docker- getting started in the wiki