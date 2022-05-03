# Terraform State

Lets look at the present state:

`terraform state list`{{execute}}

`docker ps`{{execute}}

We can kill the docker container:

`docker stop tutorial`{{execute}}

And you'll see it's still in the state list:

`terraform state list`{{execute}}

Runnng 'refresh' will refresh that terraform state (Warning: This command is deprecated)

`terraform refresh`{{execute}}


`terraform state list`{{execute}}

Lets for the state back to what it should me:

`terraform apply`{{execute}}

note that the command is requesting a port - we should have outputed a plan

`terraform state list`{{execute}}

Terraform taint will mark an object for replacement (destroy and build) at the next plan/apply

`terraform taint docker_container.nginx`{{execute}}

you can untaint using terraform untaint cmd
`terraform state list`{{execute}}

`terraform state show docker_container.nginx`{{execute}}

we can also review the whole stack state with

`terraform show`{{execute}}

`terraform plan`{{execute}}


when you run 'terraform plan' you can see in the output that the container will be replaced.

`terraform apply -var="port=8080"`{{execute}}

# terraform taint

`terraform state list`{{execute}}

`terraform taint docker_container.nginx`{{execute}}

`terraform plan -var="port=8090"`{{execute}}

Note that the top of the output shows the resource that will be replaced

`terraform apply -var="port=8090`{{execute}}

# add a variable file  (to store vars)

## remove the -var from the next section

# using a terraform plan file

`terraform plan -var="port=8080" -out myplan.tfplan`{{execute}}

you can view the contents of that plan:

`terraform show myplan.tfplan`{{execute}}

and to apply that plan:

`terraform apply myplan.tfplan`{{execute}}