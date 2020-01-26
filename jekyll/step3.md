step-by-step 6 throu 7



### Layouts   WIP moved to step 3


see
https://stackoverflow.com/questions/38891463/jekyll-default-installation-doesnt-have-layouts-directory

### WIP: this will destroy the minina layout
Lets create your 1st layout, _layouts/default.html
Layouts lets you define templates for your content, setting a layout on the front matter of the lay your working on allow you to define the layout templete for that page.

`mkdir ~/my_blog/_layouts`{{execute}}


```html
cat <<EOF > _layouts/default.html
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
Notice the two liquid cmds: page.title (from front matter) and content.
(see here for more:)[https://jekyllrb.com/docs/step-by-step/04-layouts/]






### new section

Onto datafiles,  assets

You can also include a '_data' folder in your site to include yaml, json anc csv data

```bash
mkdir ~/my_blog/_data
cat <<EOF > _data/navigation.yml
- name: Home
  link: /
- name: About
  link: /about.html
EOF
```

Jekyll makes this data file available to you at `site.data.navigation`, so lets use it in an includes file

```bash
cat <<EOF > _includes/navigation.html
<nav>
  {% for item in site.data.navigation %}
    <a href="{{ item.link }}" {% if page.url == item.link %}style="color: red;"{% endif %}>
      {{ item.name }}
    </a>
  {% endfor %}
</nav>
```


### Assets



(Lets cover the _data files folder)[https://jekyllrb.com/docs/step-by-step/06-data-files/]


Assets cover the other parts of a website, javascript, css and images
(and the assets)[https://jekyllrb.com/docs/step-by-step/07-assets/]

### Drafts

to create content that you don't want in your website, create a folder `_drafts`
The folder won't be rendered  into the web page unless you add --draft to the jekyll servce command.
* files in the draft folder don't need a date in the file name.
