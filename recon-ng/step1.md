# Recon-ng on Docker


WIP: check https://github.com/lanmaster53/recon-ng/wiki/Getting-Started#using-docker   
and match with what do do below
DO NOT Pull the docker hub image, it is the old version 4

`mkdir .recon-ng`{{execute}}
`git clone https://github.com/lanmaster53/recon-ng.git`{{execute}}
`cd recon-ng`{{execute}}
`docker build --rm -t recon-ng .`{{execute}}
`docker run --rm -it -p 5000:5000 -v $(pwd):/recon-ng -v ~/.recon-ng:/root/.recon-ng --entrypoint "./recon-ng" recon-ng`{{execute}}

WIP read the rest of the docker- getting started in the wiki