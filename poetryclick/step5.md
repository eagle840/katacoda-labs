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