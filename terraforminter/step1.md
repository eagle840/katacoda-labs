# initial setup


## install terraform
`sudo apt update`{{execute}}    

`curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -`{{execute}}    

`apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"`{{execute}}  


`apt install terraform`{{execute}}    

`terraform version`{{execute}}    

  

`terraform -install-autocomplete`{{execute}}    

`exec bash`{{execute}}

`ls`{{execute}}

# basic docker

copy the tf file in to the assets folder

!REVIEW THE .tf files before running init

`terraform init`{{execute}} 

now look at the 

`tree -a`{{execute}}

`cat .terraform.lock.hcl`{{execute}}

`terraform plan`{{execute}}    

`terraform apply`{{execute}} 

# Terraform Output

https://learn.hashicorp.com/tutorials/terraform/outputs

`nano output.tf`{{execute}}

```
output "ext_port" {
  description = "External port of docker container"
  value       =  resource.docker_container.nginx.ports.external
}
```

`terraform fmt`{{execute}}

`terraform validate`{{execute}}

`terraform init`{{execute}}

`terraform plan`{{execute}}

`terrform apply`{{execute}}

`terraform output`{{execute}}

`terrform output ext_port`{{execute}}

Starting with version 0.14, Terraform wraps string outputs in quotes by default. You can use the -raw flag when querying a specified output for machine-readable format.,,   also -json


sensitive   = true

  

   
