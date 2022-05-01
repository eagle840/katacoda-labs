# Terraform Workspaces

lets make a few adjustments so we can add a 2nd container:   

Add:

`nano var.tf`{{execute}}

```
variable "container_name" {
  type        = string
  description = "enter the container name"
}
```

add update

`nano main.tf`{{execute}}

```
resource "docker_container" "nginx" {
  image = docker_image.nginx.latest
  name  = var.container_name
  ports {
    internal = 80
    external = var.port
  }
}
```
before we output a plan file, lets create a variable file to set the variable values

>>>>>   MAKE A VARIABLE FILE 

`terraform plan -out=xxx   -varfile ==xxx`

`terraform plan -out=myplan.tfplan`{{execute}}

use container_name=mycontainer,  and port=8090

you'll notice that the docker container will have running will be replaced.

We'll create a new workspace


`terraform workspace list`{{execute}}

`terraform workspace new ws2`{{execute}}

`terraform workspace list`{{execute}}

`terraform apply "myplan.tfplan"`{{execute}}   # it won't work, so create a new plan

`terraform plan -out=myplan.tfplan`{{execute}}

`terraform apply "myplan.tfplan"`{{execute}}

`docker ps`{{execute}}  

Lets take a look at the tree structure, and you'll see an added folder for the workspace: ./terraform.tfstate.d/ws  

`tree -a` {{execute}}
 

`docker ps`{{execute}}

 # LINK TO the page running httpd

# add the index.thml to the httpd container

 