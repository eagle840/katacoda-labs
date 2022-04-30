#  advanced

Taked from:  https://github.com/Azure-Samples/flask-app-on-azure-functions


`cd ~`{{execute}}

`git clone https://github.com/Azure-Samples/flask-app-on-azure-functions.git`{{execute}}

`cd flask-app-on-azure-functions`{{execute}}

`tree`{{execute}}


`pip install --no-cache-dir -r requirements.txt`{{execute}}




# Initiate and  Run the local function

`func init --worker-runtime python --docker`{{execute}}

Run `func start`{{execute}} from within the start folder with the virtual environment activated.

DELETE NEXT LINE?
Run http://localhost:7071/api/classify?img=https://raw.githubusercontent.com/gvashishtha/functions-pytorch/master/resources/assets/Bernese-Mountain-Dog-Temperament-long.jpg

# BUILD AND RUN


`docker build . --tag azurefunc`{{execute}}

`docker run -p 8080:80 azurefunc`


