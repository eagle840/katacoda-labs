# Setup a Pulumi stack

In the section  you'll need a api key for the Pulumi website.

If you haven't already, create a Pulumi account (it's free) and create an API key. Be sure to copy it down, you won't be able to see it again in the web portal. (when you've finished the lab, you should also deplete that key since katacoda is an open environment)

create a directory

`mkdir quickstart && cd quickstart`{{execute}}


lets confirm that the k8s is up and running

`k get nodes`{{execute}}

and check to see if there are any pods, there should be none.

`k get pods`{{execute}}


`pulumi new kubernetes-python`{{execute}}


you'll be prompted for the API key, paste it in.

Enter the requested text as prompted

Lets take a look at the files created

`ls`{{execute}}

and tell Pulumi to bring the stack up

`pulumi up`{{execute}}

you should see it bring up a nginx deployment

`k get pods`{{execute}}

And you can check your pulumni account and see the details on the stack you created.