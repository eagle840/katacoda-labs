In this scenario ruby is already installed, but to install it on your system:

`apt install ruby -y`

Install jekyll (takes  a couple of minutes)

`gem install jekyll bundler`{{execute}}

Generate a Gemfile

`bundle init`{{execute}}

Edit the gemfile
CHECK THIS
`echo 'gem "jekyll"' >> Gemfile`{{execute}}

Bundle it

`bundle`{{execute}}

Create a index.html

`cat <<EOF > index.html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{ page.title }}</title>
  </head>
  <body>
    {{ content }}
  </body>
</html>
EOF`

If you need to brush up on your html, ccs and javascript,
head over to [w3schools](https://www.w3schools.com/) and checkout thier interactive tutorials

Or just copy this to create a index.html

`<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Home</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>`

and lets build, and then serve:

`jekyll build`{{execute}}


To serve this website up on the localhost only on the default 4000 port, use:
`jekyll serve`


But since we have no web browser on this host, we'll allow any connection.
`jekyll serve --host 0.0.0.0`{{execute}}
ADD AN EXIT COMMAND HERE


Open a  new terminal tab and lets check the service is running
`curl http://localhost:4000`{{execute}}


Lets open this up in a new browser tab:

https://[[HOST_SUBDOMAIN]]-4000-[[KATACODA_HOST]].environments.katacoda.com

Any changes done will automatically show (except changes to _config/yaml which needs a restart)
