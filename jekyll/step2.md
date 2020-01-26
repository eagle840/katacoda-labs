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
For this new site a theme has automatically been installed called 'minina'.
Take  a look at the _config and gem file to see where they are listed.

`cat _config.yml`{{execute}}
`cat Gemfile`{{exexute}}

Themes are used a lot in jekyll, and you'll need to read the info on it before you use it. For 'minina' see https://github.com/jekyll/minima. 

WIP: why do we need to bundle? I ran serve and it shows correct!
We'll need to rebundle jekyll to account for the new gem files.
(more about the theme)[https://rubygems.org/gems/minima]

`bundle`{{execute}}

The additional ruby gem is 'minina', which we'll take a look at a little further down.

The new site we've created is a scaffold, and you'll see that there is no _site folder in here 
and we need to create our new site with the build command:

`jekyll build`{{execute}}

`tree ~/my_blog`{{execute}}


We'll open a new terminal window and get jekyll serve running to view the site.

On the top of the terminal, next to 'terminal' click on the + sign and 'open new terminal' 
and start up the jekyll serve

`cd ~/my_blog`{{execute}}

WIP lets run this as a job in the background as opposed to a new terminal
`jekyll serve --host 0.0.0.0`{{execute}}

You should see the new content the web page you opened in the last stage.
https://[[HOST_SUBDOMAIN]]-4000-[[KATACODA_HOST]].environments.katacoda.com

Jump back to the orginal terminal 1, and we'll continue.

`cd ~/my_blog`{{execute}}

Note that jekyll should be run in the folder you have the contents in, in this case my_blog. 


### Creating Posts

Lets take a look at the webpage, you'll notice 'Posts' right in the middle, (we'll get to general pages in the next part).

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




### General Content
You'll be placing your content into 1 of two groups:
posts: in the _posts folder, these are chronlogicaly listed html or md documents, in the form YYYY-MM-DD-post-title.md - you'll see an example has already been placed, and
pages: html/md files placed anywhere in the folders


### WIP    where is this section???


### should we do nav right here?


### Includes
Another folder is the _includes, allowing you to have a repo of snippets of code to include in to other files.
`mkdir ~/my_blog/_includes`{{execute}}
and insert a nav page to include in any page.
`touch ~/my_blog/_includes/navigation.html`{{execute}}
```html
<nav>
  <a href="/" {% if page.url == "/" %}style="color: red;"{% endif %}>
    Home
  </a>
  <a href="/about.html" {% if page.url == "/about.html" %}style="color: red;"{% endif %}>
    About
  </a>
</nav>
```



(Includes)[https://jekyllrb.com/docs/step-by-step/05-includes/]



### Collections: MOVE TO LATER STEP
related documents under a collection name
[see Ben Balters blog for an overview](https://ben.balter.com/2015/02/20/jekyll-collections/)
^^^^  move this  down to step 4??  ^^^^^

