In this scenario ruby is already installed, but to install it on your system:

`apt install ruby -y`

Install jekyll (needs to be pre-installed and a cmd to check ruby)

`gem install jekyll bundler`{{execute}}

Generate a Gemfile

`bundle init`{{execute}}

Edit the gemfile
CHECK THIS
`echo 'gem "jekyll"' >> Gemfile`{{execute}}

Bundle it

`bundle`{{execute}}


use the command git clone to download your repo, and then change directory to it

Create a index.html

NEED TO CREATE

and lets build, and then serve (be sure your in the right directory)

`jekyll build`{{execute}}


To serve this website up on the localhost only, use:
`jekyll serve`{{execute}}
ADD AN EXIT COMMAND HERE

But since we have no web browser on this host, we'll allow any connection.
`jekyll serve --host 0.0.0.0`{{execute}}
ADD AN EXIT COMMAND HERE


Open a  new terminal tab and 
`curl http://localhost:4000`{{execute}}


Lets open this up in a new browser tab:

https://[[HOST_SUBDOMAIN]]-4000-[[KATACODA_HOST]].environments.katacoda.com

