# setup jenkins

Once logged into the jenkins portal, select 'install suggested plugins'

create your admin user, eg un: admin  pw: 1234  

set the name of the jenkins URL

[wip]   http://<hostname>:2119/   (2119 ?)  <= already set

'create a job' in the center section, give it a name (eg testjob) and select 'Freestyle project', then 'ok'
'create a freestyle job

Scroll down to Build, and 'add build step'/Execute shell  and enter 'date'  and 'save'

down click 'Build now' in the LHS, and below that you'll see the Build History populate

Click on the item and then 'Console Output' and you'll see that 'date' was executed 


lets take a quick poke around in the jenkins folder (connected to the jenkins container)

`ls ./jenkins/jobs`{{execute}}

and you'll see you're first job.





