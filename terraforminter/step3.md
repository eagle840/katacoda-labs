# Terraform Workspaces

add:

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


`cd ~`{{execute}}

`docker ps`{{execute}}   

`terraform workspace list`{{execute}}   

`terraform workspace `{{execute}}   

`terraform workspace -h`{{execute}}   

`terraform workspace new new1`{{execute}}   

`terraform workspace list`{{execute}}   

`docker ps`{{execute}}   

`terraform plan`{{execute}}

`terraform apply`{{execute}}