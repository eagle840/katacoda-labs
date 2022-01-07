

# setup

see:
https://docs.python.org/3/tutorial/venv.html


`python -V`{{execute}}
   
`python3 -V`{{execute}}

`ln -s /usr/bin/python3 /usr/bin/python`{{execute}}

`apt update`{{execute}}

`/usr/bin/python3 -m pip install --upgrade pip`{{execute}}

`apt install -y python3.8-venv`{{execute}}

`pip freeze`{{execute}}

# activate`{{execute}}

`python3 -m venv tutorial-env`{{execute}}

win:
    `tutorial-env\Scripts\activate.bat`

unix:
    `source tutorial-env/bin/activate`{{execute}}

`which python3`{{execute}}

`which pip`{{execute}}

`pip freeze`{{execute}}

`pip install pandas`{{execute}}

`pip install dash`{{execute}}

`pip freeze`{{execute}}

