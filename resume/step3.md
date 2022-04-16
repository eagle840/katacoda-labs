# Prepare Ubuntu server for headless chrome

In order to generate pdf's with `resume`, we  need to run the following:


`sudo apt-get update`{{execute}}

`sudo apt-get install -y libappindicator1 fonts-liberation`{{execute}}

`sudo apt-get install -f`{{execute}}

`wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`{{execute}}

`sudo dpkg -i google-chrome*.deb`{{execute}}

`apt --fix-broken install`{{execute}}

`sudo dpkg -i google-chrome*.deb`{{execute}}

`google-chrome-stable -version`{{execute}}


`export RESUME_PUPPETEER_NO_SANDBOX=1`{{execute}}

# Generate a pdf

`resume export resume.html -t jsonresume-theme-flat`{{execute}}

and view in the browser

https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/



