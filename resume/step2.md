
We need to create a resume.json file:

`resume init`{{execute}}

Enter a name, and email address

`cat resume.json`{{execute}}

We can validate the json file - no output is good

`resume validate`{{execute}}



# to use a theme

You can use a theme by looking the the npm package management siet:

https://www.npmjs.com/search?ranking=maintenance&q=jsonresume-theme

and install your choice:

`npm i jsonresume-theme-flat`{{execute}}

Now tell resume to process the json into a html document.

`resume export resume.html -t jsonresume-theme-flat`{{execute}}


# serve it - should refresh automatically

`resume serve`{{execute}}

https://[[HOST_SUBDOMAIN]]-4000-[[KATACODA_HOST]].environments.katacoda.com

or server it on an httpd serve:

`docker run -dit --name my-apache-app -p 8080:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4`{{execute}}

https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/

# lets try a different theme:

`npm i jsonresume-theme-class`{{execute}}

`resume export resume2.html -tjsonresume-theme-class`{{execute}}

Since resume serve will only show resume.html file, we'll use httpd to view the directory and choose resuem2.html

`https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/`

