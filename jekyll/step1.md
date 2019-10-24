In this scenario ruby is already installed, but to install it on your system (linux):
`apt install ruby -y`

Install jekyll (takes  a couple of minutes)
`gem install jekyll bundler`{{execute}}

Generate a Gemfile
`bundle init`{{execute}}

Edit the gemfile
`echo 'gem "jekyll"' >> Gemfile`{{execute}}

Bundle it
`bundle`{{execute}}


We could work on the pwd, but we'll create a new folder with
`jekyll new newsite`{{execute}}

and change to that directry
`cd newsite`{{execute}}

Create a index.html

```bash
cat <<EOF > index.html
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
EOF
```

If you need to brush up on your html, ccs and javascript,
head over to [w3schools](https://www.w3schools.com/) and checkout their interactive tutorials

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

and lets build, and then serve (only run it in your home folder):

`jekyll build`{{execute}}

you'll notice that a folder _site has been created. Make sure you make no changes in this folder for now, it's the content for the generated site. (the option --watch will continue to update)
Look at the index.html in _site, you'll notice its the same in your home folder.

Lets add some liquid template code. In the index.html file in your home folder (not _site - it's an easy mistake to make)

replace <h1>Hello World!</h1>       with
<h1>{{ "Hello World!" | downcase }}</h1>

run `jekyll build`{{execute}}   again
and check the _site/index.html,  and you'll see it as shown above.

We need Jekyll to process this so lets add some 'front matter' to the top of the orginal index.html (in home)

---
# front matter tells Jekyll to process Liquid
---

`jekyll build`{{execute}}
You'll now see jekyll has lower cased the whole line.
If you use 'jekyll serve' jekyll will run a webserver, and continually adjust the code as your update it.

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
