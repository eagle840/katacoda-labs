# troubleshooting poetry

`poetry debug info`{{execute}}

`poetry config --list`{{execute}}

it you not the cache setting in the config, that is the location of the virtual env bin/scripts

see https://python-poetry.org/docs/configuration/#cache-dir


if you get:

  PermissionError

  [Errno 13] Permission denied: 'pyclick/main.py'

  this is because the file isn't executable.

  Add poety run python cmd.py 

  or run poetry shell

  or set the file as exe chmod +x

  # pinning and verions

  - without a version (PyYAML), 
  - pin a version (pandas==0.23.3), 
  - specify a minimum version ('numpy>=1.14.5) 
  - or set a range of versions (matplotlib>=2.2.0,<3.0.0)

  # dependencies

pip freeze

  pip install pipdeptree

pipdeptree   
gives you a tree layout and the pack=kages that are depended on (https://github.com/naiquevin/pipdeptree)


pip show <pkg>   
shows you, 'requires' and 'Required-by' pkgs that need it

pipdeptree can allso do this, and possible conflicking dependiences
pipdeptree -p <pkg>