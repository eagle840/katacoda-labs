
This lab completements 

Github repo: https://github.com/nickmccullum/algorithmic-trading-python

youtube instructional video: https://www.youtube.com/watch?v=xfzGZB4HhEE

download the source files from:



`git clone https://github.com/nickmccullum/algorithmic-trading-python`{{execute}}

`cp sp_500_stocks.csv ./algorithmic-trading-python/starter_files/`{{execute}}


Lets update Ubuntu first:

`sudo apt-get update`{{execute}}

## install a sql

`apt install sqlite`{{execute}}

`sqlite3 -help`{{execute}}

`sqlite3 test1.db`{{execute}}

`.help`{{execute}}

`.exit`{{execute}}

check  python

`python -V`{{execute}}

WIP switch commands to python3

`python3 -V`{{execute}}

and update it:
`pip install --upgrade pip`{{execute}}

Install pandas

`pip install pandas`{{execute}}

`pip install requests==2.22.0`{{execute}}

`pip install scipy==1.5.2`{{execute}}

`pip install XlsxWriter==1.2.2`{{execute}}

`pip install yfinanace`{{execute}}

`python3 -m pip install SQLAlchemy`{{execute}}

`docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -d mysql:8.0.2`{{execute}}

`docker exec -it some-mysql mysql -uroot -p1234`{{execute}}

Info on pandas: https://pypi.org/project/pandas/

### To connect to from the host

`apt install mysql-client-core-8.0`{{execute}}

`mysql --host=127.0.0.1 -uroot -p1234  --ssl-mode=disabled`{{execute}}

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

