# Notes on this project


# NEW!
stripped down to two parts,  need to add a second (and third?) labs  so I can close this project to v1


## add

_layout    this folder contains a list of html (md?) that generates the main html for a page
            when in the front matter of a page(or post), this html will generate the html (and layput) for that page. It also includes files that that can be used with 'include tages'
            This folder allows inheritance

_includes   this folder contains  a list of html docs that cab be included with an 'include' tage
                {% include navigation.html %}  declared in other documents


katacode markdown
`this command`{{copy}}   copy to clipbord
`echo "Send Ctrl+C before running Terminal"`{{execute interrupt}}
<kbd>Ctrl</kbd>+<kbd>C</kbd>    # show keyboard keys in text
`echo "Run in Terminal 1"`{{execute T1}}

# to copy  a lrg chunk of text
<pre class="file" data-target="clipboard">
Copy Me To The Clipboard!!
</pre>

Intro
Step1: install Jekyll and generate single page
step2: generate blank (default) site, includes and layouts
step3: 




Dashboard (horizontal above the terminal)
in index.json

"environment": {
    "showdashboard": true,
    "dashboards": [{"name": "URL", "href": "https://www.google.co.uk"},
        {"name": "Port 80", "port": 80},
        {"name": "Placeholder", "href": "https://[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com"}]
}
#    Displaying External Webpages
#    Rendering Proxied Port
#    Rendering Proxied URL


Terminal Tabs
https://katacoda.com/scenario-examples/scenarios/dashboard-tabs

"environment": {
  "terminals": [{"name": "Terminal 2", "target": "host01"}]
}

