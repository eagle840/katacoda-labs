# run a cdk


`mkdir learn-terraform-docker-container`{{execute}}    

`cd learn-terraform-docker-container`{{execute}}   

`nano main.tf`{{execute}}   
copy the code below

`terraform init`{{execute}}    

`terraform plan`{{execute}}    

`terraform apply`{{execute}}    

note the new terraform state file, a json file

`tree`{{execute}}

we can list the components,

`terraform state list`{{execute}}

or get a full description of one of the compoents,

`terraform state show docker_image.nginx`{{execute}}

check running containers
`docker ps`{{execute}}   

open 8000

## Graph

lets generate a graph

we'll need to inside a pkg `apt install graphviz -y`{{execute}}

`terraform graph | dot -Tpng > graph.png`{{execute}}

and we can run a quick docker to view it

`docker run -p 80:8090 -v ./:/usr/share/nginx/html nginx`

GOTO 8090 and /graph.png

## code

```
this is a code block
why is the below not working?

terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}
```



```
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.latest
  name  = "tutorial"
  ports {
    internal = 80
    external = 8000
  }
}
```