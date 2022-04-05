

# Intro to passive recon and recon-ng

### KILL-CHAIN
- recon
- exploit
- escalate
- lateral movement
- evade
- action
recon-ng deals with the first part: recon


### MITRE PRE-ATT&CK
recon-ng excels at Technical and Personal info gathering
T1250, T1261, T1271

### Passive recon 
Using other then target

### Active
Non-malisous contact with the target, and can be tracked
You should really have permission to do this

## recon-ng interface

Once the docker container is running you should see intro logo and a command prompt.

### prompt
the cmd prompt tells you where you are in the cli   
The first part is '[recon-ng]'   
The second part shows the workspace you are in, and the third shows you the module your are in. To go back, use `'back'   
Workspaces are used to contain your work.   

help   & help (cmdName)  will show help.   
help is also context based, ie where you are in your commands.  


### database
recon-ng has a built in database that tracts information and has a preset set of tables
run `show` and you'll see the last of tables.


## Setup a workspace and recon

#### create a workspace
 Presently we are in the default workspace. Lets create a workspace for IBM and do some basic recon.
 WIP find a smaller company (results are too big)
 `workspaces create IBM`{{execute}}   
 

 #### Get seed/data


Lets enter the company into the companies table:   
 `db insert companies`{{execute}}  
  enter the company name, enter, then enter again

 `show companies`{{execute}}  to confirm

Now lets add the domain for the company (multiple if needed)

 `db insert domains`{{execute}}  ENTER, then   enter the domain, eg example.com , and any notes.

 `show domains`{{execute}}



 #### find and install modules

 Generally  you'll search the marketplace for modules, install from the marketplace, and then load that module to run it - 
 to back out of a module use `back`


 `marketplace search`{{execute}}  for all   

  ! note dependiences and keys

  For keys, you'll need to get a API key to use that module.

  module names are in the form   recon/<inputtable>-<outputTable>/<modulename>

  `marketplace search companies-`{{execute}} to find things it can do with companies

  `marketplace install whois_miner`{{execute}}

  `modules load miner`{{execute}}

  `help`{{execute}} will show context help

  `info`{{execute}}  to show info on this module

  `run`{{execute}}  to run the module against the data you already have, it'll show you the group info its inserted into each table


lets look at the contacts table that it has inserted data into

`show contacts`{{execute}}






#### Get a summary

run `dashboard`{{execute}}

#### adding API keys

load the module you want to run,
`keys list`{{execute}} will show you the key you need for the api
`keys add myapi_api keyValue`{{execute}}
`keys list`{{execute}}  to confirm
 


















