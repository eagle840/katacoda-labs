# Notes on this project

## add

_layout    this folder contains a list of html (md?) that generates the main html for a page
            when in the front matter of a page(or post), this html will generate the html (and layput) for that page. It also includes files that that can be used with 'include tages'
            This folder allows inheritance

_includes   this folder contains  a list of html docs that cab be included with an 'include' tage
                {% include navigation.html %}  declared in other documents