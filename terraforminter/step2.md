#

`terraform state list`{{execute}}

`docker ps`{{execute}}

`docker stop tutorial`{{execute}}

`terraform state list`{{execute}}

`terraform refresh`{{execute}}

`terraform apply`{{execute}}

note that the command is requesting a port - we should have outputed a plan

`terraform state list`{{execute}}

Terraform taint will mark an object for replacement (destroy and build) at the next plan/apply

`terraform taint docker_container.nginx`{{execute}}

you can untaint using terraform untaint cmd
`terraform state list`{{execute}}

`terraform show docker_container.nginx`{{execute}}

`terraform plan`{{execute}}


when you run 'terraform plan' you can see in the output that the container will be replaced.

`terraform apply -var="port=8080"`{{execute}}