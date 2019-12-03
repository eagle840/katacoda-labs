## Install Jekyll

In this scenario ruby is already installed, but to install it on your system (linux):
`apt install ruby -y`

Lets do a quick version check to  make sure ruby, and it's package manager are installed,
`ruby -v ; gem -v`{{execute}}

Install jekyll  using the ruby package manager 'gem' (takes  a couple of minutes)
`gem install jekyll bundler`{{execute}}

And check the version/install.
`jekyll -v`{{execute}}

Generate a Gemfile with:
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
    <title>Home</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>
EOF
```

If you need to brush up on your html, ccs and javascript,
head over to [w3schools](https://www.w3schools.com/) and checkout their interactive tutorials


Lets start using jekyll to  build, and then serve  our website (only run it in your home folder for now):

`jekyll build`{{execute}}

`tree`{{execute}}



you'll notice that a folder _site has been created. Make sure you make no changes in this folder for now, it's the content for the generated site. (the option --watch will continue to update)
Look at the index.html in _site, you'll notice its the same in your home folder right now. As we add content it will auto generate pages.

`cat ~/_site/index.html`{{execute}}

It should be the same as the orginal index.html


### A little bit of Liquid

Front matter in the beginning of a page tells Jekyll to process the contents of a page. This front matter can be JSON or YAML.
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
and check the _site/index.html,  and you'll see it's removed the front matter and processed Hello World to lower case.

`cat ~/_site/index.html`{{execute}}


If you use 'jekyll serve' jekyll will run a webserver (on port 4000), and continually adjust the code as you update it.

To serve this website up on the localhost only on the default 4000 port, use:
`jekyll serve`


But since we have no web browser on this host, we'll allow any connection.
`jekyll serve --host 0.0.0.0`{{execute}}

Lets open this up in a new browser tab:

https://[[HOST_SUBDOMAIN]]-4000-[[KATACODA_HOST]].environments.katacoda.com

Any changes done will automatically show (except changes to _config.yaml which needs a restart)

To stop this server, we'll be starting a new server in the next section.
`echo "Send Ctrl+C before running Terminal"`{{execute interrupt}}

Lets cleanup a little
`rm index.html; rm -r _site`{{execute}}
