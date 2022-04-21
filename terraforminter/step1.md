# initial setup


## install terraform
`sudo apt update`{{execute}}    

`curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -`{{execute}}    

`apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"`{{execute}}  


`apt install terraform`{{execute}}    

`terraform version`{{execute}}    

  

`terraform -install-autocomplete`{{execute}}    

`exec bash`{{execute}}

# Basic Setup

`ls`{{execute}}

a main file, containing the provisoners and a providers file have been provided.



`terraform init`{{execute}} 

now look at the 

`tree -a`{{execute}}

You'll set a lock file, which locks down which versions you can use, and you'll see the downloaded provider in the `.terraform` folder.

`cat .terraform.lock.hcl`{{execute}}

Notice the provider and the version and constraints.

`terraform plan`{{execute}}    

`terraform apply`{{execute}} 

and check the container is running:

`docker ps`{{execute}}

# Terraform Output

Docs: https://www.terraform.io/language/values/outputs

Learn more: https://learn.hashicorp.com/tutorials/terraform/outputs

While the outputs declaration can appear anywhere, we'll follow best practice and create an output.tf file.

`nano output.tf`{{execute}}

```
output "ext_port" {
  description = "External port of docker container"
  value       =  resource.docker_container.nginx.ports
}
```

Format the tf files:   
`terraform fmt`{{execute}}

Validate the tf files:   
`terraform validate`{{execute}}

`terraform init`{{execute}}

`terraform plan`{{execute}}


This time we run the apply, you'll see the added 'output'   
`terraform apply`{{execute}}

We can now query the output held in the state file:

`terraform output`{{execute}}

Lets dump out a set of values in json (for format them with jq)

`terraform output -json ext_port | jq`{{execute}}

Starting with version 0.14, Terraform wraps string outputs in quotes by default. You can use the -raw flag when querying a specified output for machine-readable format.,,   also -json


sensitive   = true

  

   
