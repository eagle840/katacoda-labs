
   `mkdir learn-terraform-docker-container`{{execute}}    
   17  `cd learn-terraform-docker-container`{{execute}}    
   18  `nano main.tf`{{execute}}    
   19  `terraform init`{{execute}}    
   20  `terraform plan`{{execute}}    
   21  `terraform apply`{{execute}}    
   22 ` history`{{execute}}    

  


```terraform {
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