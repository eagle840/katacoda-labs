## Install Jekyll

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




## Build out first website
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


and lets use jekyll to  build, and then serve (only run it in your home folder):

`jekyll build`{{execute}}

`tree`{{execute}}

you'll notice that a folder _site has been created. Make sure you make no changes in this folder for now, it's the content for the generated site. (the option --watch will continue to update)
Look at the index.html in _site, you'll notice its the same in your home folder.



### A little bit of Liquid

Front matter in the beginning of a page tells Jekyll to process the contents of a page.
Lets add some Liquid template code. In the index.html file in your home folder (not in _site - it's an easy mistake to make)

Add the following to the top of index.html
```
---
# front matter
---
```

and replace 
`<h1>Hello World!</h1>`  in index.html with
`<h1>{{ "Hello World!" | downcase }}</h1>`

run `jekyll build`{{execute}}   again
and check the _site/index.html,  and you'll see it as shown above.

`cat ./_site/index.html`{{execute}}
We need Jekyll to process this so lets add some 'front matter' to the top of the orginal index.html (in home)


`jekyll build`{{execute}}
You'll now see jekyll has lower cased the whole line.
If you use 'jekyll serve' jekyll will run a webserver, and continually adjust the code as your update it.

To serve this website up on the localhost only on the default 4000 port, use:
`jekyll serve`


But since we have no web browser on this host, we'll allow any connection.
`jekyll serve --host 0.0.0.0`{{execute}}

Lets open this up in a new browser tab:

https://[[HOST_SUBDOMAIN]]-4000-[[KATACODA_HOST]].environments.katacoda.com

Any changes done will automatically show (except changes to _config/yaml which needs a restart)


Open a  new terminal tab and lets check the service is running
`curl http://localhost:4000`{{execute}}

To stop this server
`clear`{{execute}}