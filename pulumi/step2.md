# Setup a Pulumi stack

In the section  you'll need a api key for the Pulumi website.

If you haven't already, create a Pulumi account (it's free) and create an API key (under settings, access tokens). Be sure to copy it down, you won't be able to see it again in the web portal. (When you've finished the lab, you should also deplete that key since katacoda is an open environment)

create a directory

`mkdir quickstart && cd quickstart`{{execute}}


lets confirm that the k8s is up and running

`kubectl get nodes`{{execute}}

and check to see if there are any pods, there should be none.

`kubectl get pods`{{execute}}


`pulumi new kubernetes-python`{{execute}}


you'll be prompted for the API key, paste it in.

Enter the requested text as prompted

Lets take a look at the files created

`ls`{{execute}}

and tell Pulumi to bring the stack up

`pulumi up`{{execute}}

You'll see a preview of the deployment and a url for the web GUI to see the status of the deployment.
You should see it bring up a nginx deployment, lets check

`kubectl get pods`{{execute}}

