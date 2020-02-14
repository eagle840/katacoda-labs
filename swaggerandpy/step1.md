# Install need components

Lets check the version of python

`python -V`{{execute}}

Let install some troubleshooting tools:

`apt install net-tools`{{execute}}

lets install some of the python packages we'll need using python's package manager pip, updating it first:

`pip install --upgrade pip`{{execute}}

`pip install  numpy flask flasgger`{{execute}}

## Install Swagger codegen

install swagger code gen to allow use to generate a basic python frame work from a swagger configuration file. Swagger code gen requires Java 7+

`java --version`{{execute}}

`wget https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.12/swagger-codegen-cli-2.4.12.jar -O swagger-codegen-cli.jar`{{execute}}

and check the help function works.

`java -jar swagger-codegen-cli.jar help`{{execute}}

We'll be using  bhattbhavesh91/ swagger-python-flask-app demo on github, he also as a video on this.
https://www.youtube.com/watch?v=rIsEbsvuOlM

The help page for codegen: https://swagger.io/docs/open-source-tools/swagger-codegen/

`git clone https://github.com/bhattbhavesh91/swagger-python-flask-app.git`{{execute}}

You can also use the codegen on the editor.swagger.io page, and it will gnerate the code/files and allow you to download them.

and move into the folder we'll be using

`cd swagger-python-flask-app/swagger_with_flask/`{{execute}}