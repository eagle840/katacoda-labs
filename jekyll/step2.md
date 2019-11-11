step-by-step 2 thro 5

### new blog
Lets start an entirely new site with the command:
`jekyll new my_blog`{{execute}}
You'll notice a new folder my_blog creater with jekyll creating some default content in it

`tree ~/my_blog`{{execute}}

You'll also markdown files in here, jekyll process' these into html files for the website.



lets add 'hello world', or Feel free to try your own content.



We'll open a new terminal window and get jekyll serve running
On the top of the terminal, next to 'terminal' click on the + sign and 'open new terminal' 
and start up the jekyll serve
`jekyll serve --host 0.0.0.0`{{execute}}
You should see the new content the web page you opened in the last stage.
https://[[HOST_SUBDOMAIN]]-4000-[[KATACODA_HOST]].environments.katacoda.com

Jump back to the orginal window, and we''l continue.

### Layouts
Lets create your 1st layout, _layouts/default.html
Layouts lets you define templates for your content, setting a layout on the front matter of the lay your working on allow you to define the layout templete for that page.

`mkdir ~/my_blog/_layouts`{{execute}}

and define our 1st layout of 
`touch #/my_site/_layouts/default.html`

```html
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
```
Notice the two liquid cmds: page.title (from front matter) and content.
(see here for more:)[https://jekyllrb.com/docs/step-by-step/04-layouts/]



### General Content
You'll be placing your content into 1 of two groups:
posts: in the _posts folder, these are chronlogicaly listed html or md documents, in the form YYYY-MM-DD-post-title.md - you'll see an example has already been placed, and
pages: html/md files placed anywhere in the folders

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

