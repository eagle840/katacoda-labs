# adding extra agents

be sure you changed the execstart on step 1

## Add the Docker Plugin

in jenkins, select 'Manage Jenkins' > 'Manage Plugins'

click on the available tab and enter 'docker' in the search field and select just 'Docker'

click 'Download now and install after reboot', check the boc 'Restart jenkins...' when shown and jenkins will restart

katacode will prompt you to connect to the port again (9080) - wait 30 seconds - click 'display port' and login with un/pw (admin/1234)

## Config Jenkins to startup Docker Agents

goto 'manage jenkins' > 'manage nodes and clouds'

click on 'configure clouds' on LHS

on the drop-down select 'docker' and the page will refresh with more content

Select 'Docker Cloud Details'

in the Docker Host URI, enter: 'tcp://host.docker.internal:2375' (a special dns entry for the host)
[WIP] above does not work, however pull the host IP and it it'll work. Need to find out why host.docker.internal isn't in the hosts file

and click 'test connection' and you should get back the API version

check 'Enabled'   
check 'Expose DOCKER_HOST'

now click on 'Docker Agent Templates..' => 'Add Docker Template'

Give it the label  'Agent', and check 'Enabled', and Name it 'Jenkins Agent' and enter the docker image (the same as the one we used in step 1) 'jenkins/jenkins:2.255'

Set the instance capacity to '10'

set the Remote File system root  (check this works) '/var/jenkins_home'

finally check save


# set a job to use this agent

Open your job configuration and click 'Restrict where this project can be run' in the General section, and set it to 'Agent' , the same label we gave it earlier - and 'save'

running `docker ps -a` from the terminal, you should see the extra docker container

If your job doesn't start make sure that you have enabled the node cloud template from above.

You can also see the docker activity in the Jenkins System Log (manage jenkins > Status Info > System Log)

# Select your docker image for the task at hand

in this tutorial we used the jenkins image we orginally pulled down, but you can rebuild the jenkins image to add the programs/features you need

