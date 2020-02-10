

Lets update Ubuntu first:

`sudo apt-get update`{{execute}}

check  python

`python -V`{{execute}}

`python3 -V`{{execute}}


For full functionality, spark needs java 8

`java -version`{{execute}}

We'll also need python:
`python -V`{{execute}}

and update it:
`pip install --upgrade pip`{{execute}}

Note: JupyterLab is the new and upgraded version of Jypyter Note

WIP   USE NEXT LINE `python -m pip install findspark`
WIP `pip3 install findspark`
WIP `pip install findspark`

`pip install jupyterlab`{{execute}}


lets start jupyter with the --ip option, since the default it only for localhost:888

`jupyter lab --allow-root --no-browser --ip=0.0.0.0`{{execute}}

In the stdout you'll see the url and token needed to access the website.

But we can get the token with this command as well:

`cat .local/share/jupyter/runtime/nbserver-*.json | jq .token -r`{{execute T2}}

and connect to the ui

 https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com

 In the left hand side you'll see the spark file we downloaded earlier, and lets open a Notebook.
 You'll see the notebook added to the file list







# install 

we'll be using jupyter classic in this lab

https://jupyter.org/install

`pip install notebook`{{execute}}

what start up options do we have:

`jupyter notebook -h`{{execute}}


WIP: see next page for error
use jupyter.org  
use clasic

run 

`jupyter notebook` # need root access

`jupyter notebook --allow-root --ip=0.0.0.0`

you need the token to login to page

insert url for page here