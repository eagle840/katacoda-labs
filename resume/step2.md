
We need to create a resume.json file:

`resume init`{{execute}}

Enter a name, and email address

`cat resume.json`{{execute}}

We can validate the json file - no output is good

`resume validate`{{execute}}

`resume export index.html -f html`{{execute}}

`docker run -dit --name my-apache-app -p 8080:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4`{{execute}}


# to use a theme

https://www.npmjs.com/search?ranking=maintenance&q=jsonresume-theme

`npm i jsonresume-theme-flat`{{execute}}

`resume export resume.html -t jsonresume-theme-flat`{{execute}}

# serve it - should refresh automatically

`resume serve`{{execute}}

or server it on an httpd serve:

`docker run -dit --name my-apache-app -p 8080:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4`{{execute}}


