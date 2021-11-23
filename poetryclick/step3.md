# part 3
https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-3/

`tree`{{execute}}

`poetry build`{{execute}}

You'll see the build files in the dist folder, including the wheel file

`tree`{{execute}}

To publish your project to Pipy
`poetry publish `
`poetry publish --build`


`pip install <project name>`


# working with a downloaded package (made with poetry)

We'll be using the same package from the demo page:

https://pypi.org/project/how-long/#files   

`cd ~`{{execute}}

`wget https://files.pythonhosted.org/packages/f1/bc/7b3ac4a6499a333045c8adf6207983f00cb36b9d787e65cceddb5fe093a0/how-long-0.1.2.tar.gz`{{execute}}


`tar -zxvf how-long-0.1.2.tar.gz`{{execute}}

`cd how-long-0.1.2/`{{execute}}

`tree`{{execute}}

`poetry check`{{execute}}

`poetry install `{{execute}}

`poetry build`{{execute}}

to install the wheel using pip

`pip install ./dist/how_long-0.1.2-py3-none-any.whl`{{execute}}