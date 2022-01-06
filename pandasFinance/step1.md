
This lab completements 

Github repo: https://github.com/nickmccullum/algorithmic-trading-python

youtube instructional video: https://www.youtube.com/watch?v=xfzGZB4HhEE

download the source files from:

https://drive.google.com/file/d/1ZJSpbY69DVckVZlO9cC6KkgfSufybcHN/view?usp=sharing

`wget https://drive.google.com/file/d/1ZJSpbY69DVckVZlO9cC6KkgfSufybcHN/view?usp=sharing`{{execute}}


Lets update Ubuntu first:

`sudo apt-get update`{{execute}}

check  python

`python -V`{{execute}}

WIP switch commands to python3

`python3 -V`{{execute}}

and update it:
`pip install --upgrade pip`{{execute}}

Install pandas

`pip install pandas`{{execute}}

Info on pandas: https://pypi.org/project/pandas/

Note that there webpage and docs are linked on this page

Note: JupyterLab is the new and upgraded version of Jypyter Note

`pip install jupyterlab`{{execute}}

lets start jupyter with the --ip option, since the default it only for localhost:888

`jupyter lab --allow-root --no-browser --ip=0.0.0.0 &`{{execute}}


In the stdout you'll see the url and token needed to access the website, copy it (ctrl-insert)

Once you copy the token, goto the following link and copy the token (shift-insert)

 https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com

If you can't find the token, the following cmd will exe in a seperate terminal and pull the token 

`cat /root/.local/share/jupyter/runtime/jpserver-*.json | jq .token -r`{{execute T2}}

