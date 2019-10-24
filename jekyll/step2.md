step-by-step 2 thro 5



After running the build/serve from the last step, you'll notice that it was generated a _site folder.
Do not change anything in here, since it may mess things up.
Basicly it's taking everything in the root folder and processing most of the files/folders, with the exception of my _site folder.

You'll see that Jekyll has directly place the index.html into the site. For jekyll to process a file we'll need to add some 'front matter'
---
# front matter goes here, usually key:value 
---
rest of html or md here which may include instruction.


Lets learn a little about the Liquid Templating language at:
[Jekyll step-by-step step 2 - Liquid](https://jekyllrb.com/docs/step-by-step/02-liquid/)

Feel free to try out adding some changes .

You'll be placing your content into 1 of two groups:
posts: in the _posts folder, these are chronlogicaly listed html or md documents, in the form YYYY-MM-DD-post-title.md
and pages: html/md files placed anywhere in the folders

But before we add that, lets go over the _layouts folder.
This is going to be basicly the main templates for generating pages,
(see here for more:)[https://jekyllrb.com/docs/step-by-step/04-layouts/]

CREATE _layout folder
add html


Another folder is the _includes, allowing you to have a repo of snippets of code to include in to other files.
(Includes)[https://jekyllrb.com/docs/step-by-step/05-includes/]



collections: related documents under a collection name
[see Ben Balters blog for an overview](https://ben.balter.com/2015/02/20/jekyll-collections/)
^^^^  move this  down to step 4??  ^^^^^

