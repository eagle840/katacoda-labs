#  adding vars file

see: https://www.terraform.io/docs/language/values/variables.html

lets create another file var.tf that includes our variables

`nano var.tf`{{execute}}

in this first file, it will ask for the port number when tf plan/apply is run



```
variable "port" {
  type = number
}
```

`terraform apply`{{execute}}

lets check that the docker port has been ajusted:
`docker ps`{{execute}}


```
variable "image_id" {
  type = string
}


variable "docker_ports" {
  type = list(object({
    internal = number
    external = number
    protocol = string
  }))
  default = [
    {
      internal = 8300
      external = 8300
      protocol = "tcp"
    }
  ]
}
```{{copy}}
