# Update and check python

update the python pip repo

`apt-get update -y`{{execute}}

check we have ver 3.6+

`python3 -V`{{execute}}

check pip 

`pip -V`{{execute}}

update pip

`/usr/bin/python3 -m pip install --upgrade pip`{{execute}}

install venv

`apt-get install python3-venv`{{execute}}

install pulumi

`curl -fsSL https://get.pulumi.com | sh`{{execute}}

restart the shell

`exec $SHELL`{{execute}}

create a directory

`mkdir quickstart && cd quickstart`{{execute}}

`pulumi new kubernetes-python`{{execute}}
