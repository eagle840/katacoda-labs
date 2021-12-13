#  adding vars file

see: https://www.terraform.io/docs/language/values/variables.html

lets create another file var.tf that includes our variables


```sh
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
```
