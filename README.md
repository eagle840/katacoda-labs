# katacoda-labs
Katacoda scenarios code 

## katacoda
Provides an enviroment for running labs and training.
The code in this repo link over to https://www.katacoda.com/ir4engineer


## notes on getting katacoda working

*[rtfm @ www.katacoda.com/docs](https://www.katacoda.com/docs)*

1. need a github account, and understand how to use git
2. need to setup webhook between git and katacoda (see your katacoda profile)
3. need to install nodejs to use the katacoda cli  [Install instructions/download at nodejs.org](nodejs.org)
4. command to install Katacode cli, run at the command line:  npm install katacoda-cli --global

## run katacode cli to generate a scenerio folder 
1. help cmd: katacoda help
2. create your scenario folder and files with cmd:  `katacoda scenarios:create`
    (when asked,  'friendURL' is local folder name to create)
3. Sync with your github as needed, katacoda will automatically pull the code.
4. You should see your 1st katacode scenario show up under your profile.

Useful training/coding links:
* [Getting started - create scenario-101](https://katacoda.com/scenario-examples/scenarios/create-scenario-101)
* [A list of scenarios to help you get started using Katacoda](https://katacoda.com/scenario-examples)
* [The github repo for these scenarios](https://github.com/katacoda/scenario-examples)
* [O'Reilly Katacoda Authoring Guide](https://docs.google.com/document/d/14rudtruZQhRxvD3zcR3g75j5nuOgKGz4CYk8hdhaV-w/edit)
* [Creating Katacoda Content](https://www.katacoda.community/welcome.html)
