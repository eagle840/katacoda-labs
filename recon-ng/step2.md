

### KILL-CHAIN
- recon
- exploit
- escalate
- lateral movement
- evade
- action

### MITRE PRE-ATT&CK
recon-ng excels at Technical and Personal info gathering
T1250, T1261, T1271

### Passive recon 
Using other then target

### Active
Non-malisous contact with the target, and can be tracked
You should really have permission to do this

## recon-ng interface

### prompt
the cmd prompt gives you a global context.
The first part is '[recon-ng]'
The second part shows the workspace you are in.
Workspaces are used to contain your work.

help   & help <cmdName>  will show help
help is also context based, ie where you are in your commands


### Steps

#### create a workspace
 `workspaces create <workspaceName>`
 ?? is this actually a SQL db ??
 ? has tables - shown in the resources folder ?

 #### Get seed/data

 `db insert companies` enter
 enter the company name, enter, then enter again

 `show companies`  to confirm

 #### find and install modules

 General you'll search the marketplace, install from the marketplace, and then load that module to run it 
 to back out of a module use `back`


 `marketplace search`  for all   

  ! note dependiences and keys

  module names are in the form   recon/<inputtable>-<outputTable>/<modulename>

  `marketplace search companies-` to find things it can fo with companies

  `marketplace install whois_miner`

  `modules load miner`

  `help` will show context help

  `info`  to show info on this module

  `run`  to run the module against the data you already have, it'll show you the group info its inserted into each table


lets look at the contacts table that it has inserted data into

`show contacts`

See any domains into the list of contacts? insert them into the db

`db insert domains`  ENTER, then   enter the domain, eg example.com , and any notes.

Lets search the marketplace to run modules against the contacts

`marketplace search contacts-`

Lets install `marketplace install scylla`   which will install the 2 modules with scylla in their name

`modules load recon/cont` and use tab completion

run `info` to look at info on it

`run` to run module, and not the data groups added into the tables

lets load and run the other scylla module

`module load recon/doma` and use tab completion

and run it `run`

#### Get a summary

run `dashboard`

#### adding API keys

load the module you want to run,
`keys list` will show you the key you need for the api
`keys add myapi_api keyValue`
`keys list`  to confirm
 


















