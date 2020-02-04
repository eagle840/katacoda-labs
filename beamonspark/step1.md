Let's first update Ubunte

`apt update`{{execute}}

and check requirements:

`python --version`{{execute}}      #2.7+ or 3.5+

`pip --version`{{execute}}

If less than v7 run

`pip install --upgrade pip`{{execute}}

Install Python virtual environment

`pip install --upgrade virtualenv`{{execute}}

Create and activate a virtual environment

`virtualenv /path/to/directory`{{execute}}

`. /path/to/directory/bin/activate`{{execute}}

And install apache-beam for python

`pip install apache-beam`{{execute}}



