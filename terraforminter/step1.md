# initial setup


## install terraform
`sudo apt update`{{execute}}    

`curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -`{{execute}}    

`apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"`{{execute}}  


`apt install terraform`{{execute}}    

`terraform version`{{execute}}    

  

`terraform -install-autocomplete`{{execute}}    

`ls`{{execute}}

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

  

   
