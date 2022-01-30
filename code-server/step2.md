#Set up a python env with pyenv


Not sure why this line here
`#apt  install -y --skip-broken git gcc zlib-devel bzip2-devel readline-devel sqlite-devel`{{execute}}

`git clone https://github.com/pyenv/pyenv.git ~/.pyenv`{{execute}}

`echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc`{{execute}}
`echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc`{{execute}}
`echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc`{{execute}}

`exec $SHELL`{{execute}}

`pyenv install 3.7.6`{{execute}}

`pyenv versions`{{execute}}

To change our active version, we'll use pyenv shell <VERSION>:

`pyenv shell 3.7.6`{{execute}}

`python --version`{{execute}}

`pip3.7 install --upgrade pip`{{execute}}