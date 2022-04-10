
see if you can deploy an azure functions container with a python script (lambda)

`docker run --rm -p 8080:80 mcr.microsoft.com/azure-functions/dotnet:3.0`

now access that webpage at 8080



see https://hub.docker.com/_/microsoft-azure-functions


### remove to a seperate tutorial

# install func tools

see https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Clinux%2Ccsharp%2Cportal%2Cbash#v2

`curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg`{{execute}}

`sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'`{{execute}}

`sudo apt-get update`{{execute}}

`sudo apt-get install azure-functions-core-tools-4`{{execute}}

# create a custom image for docker

see:  https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image?tabs=in-process%2Cbash%2Cazure-cli&pivots=programming-language-python


`mkdir ~/azurefunc`{{execute}}

`cd ~/azurefunc`{{execute}}

`func init --worker-runtime python --docker`{{execute}}

`ls`{{execute}}

`func new --name HttpExample --template "HTTP trigger" --authlevel anonymous`{{execute}}

`func start`{{execcute}}
   
`curl http://localhost:7071/api/HttpExample?name=Functions`{{execute}}



# build and run docker image

`docker build . --tag func`{{execute}}

`docker run -p 8080:80  func`


https://2886928389-8080-cykoria04.environments.katacoda.com/api/HttpExample?name=Functions


