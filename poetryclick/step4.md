# testing

Poetry adds the scaffolding for tests, and includes creating a test folder

example to add
```
from greet.location import greet

def test_greet():
    result = greet("America/New_York")
    assert "New York!" in result
```

to run:

inside  the shell: `pytest`
outside the shell: `poetry run pytest`

for testing a cli see 
https://dev.to/bowmanjd/build-command-line-tools-with-python-poetry-4mnc

# turning python into a cli

in pyproject.toml

```YAML
[tool.poetry.scripts]
greet = "greet.location:cli"
```

the value can be read as: package.submodule:function

rerun: `poetry install`

run the cmd   
inside poetry shell `greet Africa/Addis_Ababa`
outside shell: poetry `run greet Africa/Addis_Ababa`

# using click

https://dev.to/bowmanjd/build-a-command-line-interface-with-python-poetry-and-click-1f5k



poetry new --name greet --src clickgreet

cd clickgreet

### pull the code

poetry add arrow click

### add to the pyproject

poetry install


### continue page
