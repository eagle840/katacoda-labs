# New poetry project

# part 1

Poetry can create a new scaffold for us for a new project

`poetry new pyclick`{{execute}}

`cd pyclick`{{execute}}

`tree`{{execute}}

`poetry install`{{execute}}

`poetry add click coo`{{execute}}

`poetry add -D flake8 mypy`{{execute}}

`poetry add -D black --allow-prereleases`{{execute}}

# is no longer in prerelease

`poetry remove coo`{{execute}}

`poetry remove -D mypy`{{execute}}

# Starting an virtual envirnoment

`poetry shell`{{execute}}

Run `which poetry`{{execute}} to show where the python binary is.

Exit the shell:  `exit`{{execute}}

and run  `which poetry`{{execute}} again



# Two ways to start python

`poetry run  python`

`poetry install`{{execute}}

`poetry shell`{{execute}}

Note that the command line now contains the python 

`poetry run python pyclick/hello.py --count=3`{{execute}}


to exit out of the poetry shell

`exit`{{execute}}

```
poetry new [package-name]	Start a new Python Project.
poetry init	Create a pyproject.toml file interactively.
poetry install	Install the packages inside the pyproject.toml file.
poetry add [package-name]	Add a package to a Virtual Environment.
poetry add -D [package-name]	Add a dev package to a Virtual Environment.
poetry remove [package-name]	Remove a package from a Virtual Environment.
poetry remove -D [package-name]	Remove a dev package from a Virtual Environment.
poetry self:update
```

# part 2

https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-2/

`poetry update`{{execute}}

IN VSC

poetry shell   
code .

# first click program

UPDATE THIS SECTION FROM YOUR NOTES 

`nano pyclick/hello.py`{{execute}}


```
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()

```
GET PYTHON RUN WORKING

`poetry run python pyclick/hello.py --count=3`{{execute}}

`python hello.py --count=3`{{execute}}

`python hello.py --help`{{execute}}