# setup Node and the resume-cli program

`curl -fsSL https://deb.nodesource.com/setup_16.x | bash -`{{execute}}

`apt-get install -y nodejs`{{execute}}

`node -v`{{execute}}

`mkdir myresume`{{execute}}

`cd myresume`{{execute}}

`npm install -g npm@latest`{{execute}}

`npm install puppeteer --unsafe-perm=true --allow-root`{{execute}}

`resume `{{execute}}
