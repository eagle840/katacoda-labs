
see if you can deploy an azure functions container with a python script (lambda)

`docker run --rm -p 8080:80 mcr.microsoft.com/azure-functions/dotnet:3.0`{{execute}}

now access that webpage at 8080



see https://hub.docker.com/_/microsoft-azure-functions


### remove to a seperate tutorial

# install func tools

see https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Clinux%2Ccsharp%2Cportal%2Cbash#v2

   45  curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
   46  sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
   47  sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'
   48  sudo apt-get update
   49  sudo apt-get install azure-functions-core-tools-4

# create a custom image for docker

see:  https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image?tabs=in-process%2Cbash%2Cazure-cli&pivots=programming-language-python


   53  mkdir ~/azurefunc
   54  cd ~/azurefunc
   55  func init --worker-runtime python --docker
   56  ls
   57  func new --name HttpExample --template "HTTP trigger" --authlevel anonymous
   
   60  curl http://localhost:7071/api/HttpExample?name=Functions
   61  history

# build and run docker image

docker build . --tag func



