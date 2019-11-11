step-by-step 2 thro 5

### new blog
Lets start an entirely new site with the command:
`jekyll new my_blog`{{execute}}
You'll notice a new folder my_blog creater with jekyll creating some default content in it

Lets quickly copy index over to the new site and delete the orginal content.
`cp ~/index.html ~/my_blog/index.html`{{execute}}
`rm -r _site`{{execute}}
`rm _config.yaml`{{exeute}}


rest of html or md here which may include instruction.
Two of the most command used K:V pairs used are: title and layout.
With layout, you should have a _layouts folder with files of the same name.

Lets learn a little about the Liquid Templating language at:
[Jekyll step-by-step step 2 - Liquid](https://jekyllrb.com/docs/step-by-step/02-liquid/)

Feel free to try out adding some changes .

### Layouts
Lets create your 1st layout, _layouts/default.html

`mkdir ~/_layouts`{{execute}}

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

### General Content
You'll be placing your content into 1 of two groups:
posts: in the _posts folder, these are chronlogicaly listed html or md documents, in the form YYYY-MM-DD-post-title.md
and pages: html/md files placed anywhere in the folders

But before we add that, lets go over the _layouts folder.
This is going to be basicly the main templates for generating pages,
(see here for more:)[https://jekyllrb.com/docs/step-by-step/04-layouts/]

### Includes
Another folder is the _includes, allowing you to have a repo of snippets of code to include in to other files.
(Includes)[https://jekyllrb.com/docs/step-by-step/05-includes/]



### Collections: MOVE TO LATER STEP
related documents under a collection name
[see Ben Balters blog for an overview](https://ben.balter.com/2015/02/20/jekyll-collections/)
^^^^  move this  down to step 4??  ^^^^^

