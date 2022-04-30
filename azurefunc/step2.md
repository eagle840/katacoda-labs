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



# BUILD AND RUN


`docker build . --tag azurefunc`{{execute}}

`docker run -p 8080:80 azurefunc`{{execute}}

`https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/`{{execute}}


