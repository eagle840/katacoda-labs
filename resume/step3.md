# Prepare Ubuntu server for headless chrome

In order to generate pdf's with `resume`, we  need to run the following:


`wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`{{execute}}

`sudo apt install -y ./google-chrome-stable_current_amd64.deb`{{execute}}

`google-chrome-stable -version`{{execute}}


`export RESUME_PUPPETEER_NO_SANDBOX=1`{{execute}}

# Generate a pdf

`resume export resume.pdf -t jsonresume-theme-flat`{{execute}}

and view in the browser

https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/



