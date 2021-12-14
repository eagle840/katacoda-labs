

 

instead, copy this:   
https://click.palletsprojects.com/en/8.0.x/commands/#custom-multi-commands


`which python3`{{execute}}

`ln -s /usr/bin/python3 /usr/bin/python`{{execute}}


`curl -fsSL https://code-server.dev/install.sh | sh`{{execute}}

`code-server --bind-addr 0.0.0.0:8080`{{execute}}

`cat .config/code-server/config.yaml`{{execute}}



https://click.palletsprojects.com/en/8.0.x/commands/#custom-multi-commands

https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-1/

# Install poetry

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`{{execute}}

`source $HOME/.poetry/env`{{execute}}

If you want to run poetry install the code server terminal, you'll need to run:

`source $HOME/.poetry/env`
 

`poetry -h`{{execute}}

 
