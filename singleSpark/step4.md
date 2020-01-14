# Install jupyter and run a few tests

We've already confirmed that we have the correct version of java and python installed, we'll now install `findspark' to help jupyter work with spark and then install that

wip `python -m pip install findspark`{{execute}}
or `pip3 install findspark`{{execute}}

`pip install jupyterlab`{{execute}}
wip: appears to be running on localhost:4040 only, change to allow internet
`jupyter lab` or  notebook

lets start jupyter with the --ip option, since the default it only for localhost
`jupyter lab --allow-root --ip=0.0.0.0`{{execute}}
wip: cmd automatically opens a browser (lync) find option to this


after starting it'll give you a token to log in with

- starts on port 8888

and connect to the ui
 https://[[HOST_SUBDOMAIN]]-4040-[[KATACODA_HOST]].environments.katacoda.com
