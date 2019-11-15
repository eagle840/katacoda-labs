step-by-step 6 throu 7

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
