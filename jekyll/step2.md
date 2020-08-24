step-by-step 2 thro 5

### new blog
Lets start an entirely new site with the command:
`jekyll new my_blog`{{execute}}

You'll notice a new folder, my_blog created with jekyll creating some default content in it

Lets cd to that folder and take a look
`cd ~/my_blog`{{execute}}

`tree ~/my_blog`{{execute}}

The `new` command has automatically created the gem files, you'll also note markdown/html files in here, 
and an additional ruby gem (package) has been added to the gemfile to add a theme to the site - which was been configured into the _config file.
For this new site a theme has automatically been installed called 'minima'.
Take  a look at the _config and gem file to see where they are listed.

`cat _config.yml`{{execute}}
`cat Gemfile`{{execute}}

Lets take a look at the gem file for minima, note that it's version 2.5.
`gem list --local | grep minima`{{execute}}

Themes are used a lot in jekyll, and you'll need to read the info on it before you use it. For 'minima' see https://github.com/jekyll/minima. You'll need to pay attention to the version you're using since they work differently.

WIP https://github.com/jekyll/minima/blob/v2.5.0/README.md


Lets run this as a job in the background as opposed to a new terminal
`jekyll serve --host 0.0.0.0 &`{{execute}}

You should see the new content, with the theme
https://[[HOST_SUBDOMAIN]]-4000-[[KATACODA_HOST]].environments.katacoda.com

Jump back to the orginal terminal 1, and we'll continue.

`cd ~/my_blog`{{execute}}




### Creating Posts

Lets take a look at the webpage, you'll notice 'Posts' right in the middle, 

Posts are all kept in the _post folder, as you can see there is one already there.

`tree`{{execute}}

Lets add another post, note the format of the file name: YYYY-MM-DD-post-title.md, which is required. (spaces should be replaces with dashes)

```html
cat <<EOF > _posts/2018-08-20-bananas.md
---
layout: post
author: jill
---
A banana is an edible fruit - botanically a berry - produced by several kinds
of large herbaceous flowering plants in the genus Musa.

In some countries, bananas used for cooking may be called "plantains",
distinguishing them from dessert bananas. The fruit is variable in size, color,
and firmness, but is usually elongated and curved, with soft flesh rich in
starch covered with a rind, which may be green, yellow, red, purple, or brown
when ripe.
EOF
```

refreshing the web page, you'll see the post added.




