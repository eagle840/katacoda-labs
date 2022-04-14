`resume init`{{execute}}

`resume export index.html -f html`{{execute}}

`docker run -dit --name my-apache-app -p 8080:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4`{{execute}}