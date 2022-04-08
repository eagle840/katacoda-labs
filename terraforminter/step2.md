# modules

`mkdir modules`{{execute}}

`cd modules`{{execute}}

`mkdir nginxsite`{{execute}}

`cd nginxsite`{{execute}}

A typical module contains:

```
.
├── LICENSE
├── README.md
├── main.tf
├── variables.tf
├── outputs.tf
```

`nano nginxsite.tf`{{execute}}

```
code
```

# create a file for the website


```
resource "local_file" "foo" {
    content     = "foo!"
    filename = "${path.module}/foo.bar"
}
```

# Call a module

in the main file, you'll call a module, using the `module` keyword


```
`module "anyName" {
    source = "<path>/folder"
    variable = value #the variables in the varibles.tf file
    #any variables left out, will be requested for
}

```

https://registry.terraform.io/providers/hashicorp/local/latest/docs/resources/file


In the main stack, if you want to use the output of a module
EG:


```
resource "aws ebs" "main" {
    instance = module.anyName.<varible_name>
}
```