Install ruby and jekyll

`apt install ruby -y'{{execute}}

Install jekyll

'gem install jekyll bundler'{{execute}}

Generate a Gemfile

`bundle init`{{execute}}

Edit the gemfile
CHECK THIS
`echo 'gem "jekyll"' >> Gemfile

Bundle it

`bundle'{{execute}}

Create a index.html

NEED TO CREATE

and lets build, and then serve:

`jekyll build`{{execute}}

`jekyll serve`{{execute}}

SHOULD WE JOB THE ABOVE?
Open a  new terminal tab
and 
`curl http://localhost:4000`{{execute}}


Lets open this up in a new browser tab:

https://[[HOST_SUBDOMAIN]]-4000-[[KATACODA_HOST]].environments.katacoda.com