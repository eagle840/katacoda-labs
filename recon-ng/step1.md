# Recon-ng on Docker - build and run the image


see https://github.com/lanmaster53/recon-ng


Lets pull the repo:
`git clone https://github.com/lanmaster53/recon-ng.git`{{execute}}   

`cd recon-ng`{{execute}}   

and build an image:
`docker build --rm -t recon-ng .`{{execute}}   

and run it:
`docker run --rm -it -p 5000:5000 -v $(pwd):/recon-ng -v ~/.recon-ng:/root/.recon-ng --entrypoint "./recon-ng" recon-ng`{{execute}}   


