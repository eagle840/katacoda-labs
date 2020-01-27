# Install jupyter and run the same python commands

We've already confirmed that we have the correct version of java and python installed, we'll now install `findspark' to help jupyter work with spark and then install that

wip  USE NEXT LINE `python -m pip install findspark`{{execute}}
or `pip3 install findspark`{{execute}}

`pip3 install jupyterlab`{{execute}}


lets start jupyter with the --ip option, since the default it only for localhost:888

`jupyter lab --allow-root --no-browser --ip=0.0.0.0`{{execute}}

You'll need the token outputted from the cmd to login to Jupyterlab.


and connect to the ui

 https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com
