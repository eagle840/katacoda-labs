# modules

In terraform, a 'resource' is part of a 'provider', for example, for the docker provider, we  can see what resources we can use my looking at that resources docs [Docker Provider](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs) - in the left hand side you can expand out the list of resources.

In this section will create a local custom type of resource called a module, which it's self can use other modules and resources. "Modules are self-contained packages of Terraform configurations that are managed as a group."


The Terraform repo contains an extensive collections of [modules](https://registry.terraform.io/browse/modules) that have been uploaded, but you can store modules in many other places.

To learn even more see the module learning docs: https://learn.hashicorp.com/tutorials/terraform/module?in=terraform/modules


We'll create a folder to store the modules:   
`mkdir modules`{{execute}}

`cd modules`{{execute}}


and create a new module(folder) called 'nginxsite', just a simple webserver, with a static html file:   
`mkdir nginxsite`{{execute}}

`cd nginxsite`{{execute}}

A typical module will contain:

```
.
├── LICENSE
├── README.md
├── main.tf
├── variables.tf
├── outputs.tf
```

# create module   -- JUST KEEP TE nginx container in the main for now

WIP `nano nginxsite.tf`

```
code
```

# create a file for the website

`nano index.html`{{execute}}   

add the code:
```
<!DOCTYPE html>
<html>
    <head>
        <title>Example</title>
    </head>
    <body>
        <p>Hello world!</p>
    </body>
</html>
```

`nano pagesource.tf`{{execute}}   
```
resource "local_file" "index" {
    content     = "Index"
    filename = "${path.module}/index.html"
}
```

# Call a module

in the main root tf file, you'll call a module, using the `module` keyword


```
`module "anyName" {
    source = "<path>/folder"
    variable = value #the variables in the varibles.tf file
    #any variables left out, will be requested for
}

```
`cd ~`{{execute}}

change the main.tf file to include the module:

`nano main.tf`{{execute}}

```
module "mywebpage" {
    source = "./modules/nginxsite" 
}
```
?is nginxsite the name of the 'module' or the dir?

Because this is an added module/resource, we can rerun init, or get to install the modules/providers

`terraform get`{{execute}}


Running plan will now show the added module/file
`terraform plan`{{execute}}

`terraform apply`{{execute}}

You'll now see the index.html added to the module directory

`tree`{{execute}}



# add the resource into the contain binding volume

https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/container

------------------------------

Pulling output from  module.

In the resource you want to use a module output

    syntax: module.<MODULE NAME>.<OUTPUT NAME>

    x = module.<y1>.<y2>

y1: is the name of the module you called it in the root tf foleder
y2: is the outputname you used in the <module>.<var> 
--------------------------------
If the module is actually in the terraform repo, you'll use the name of the module instead of <path> , you'll also have to include a key=value for the version number.

https://registry.terraform.io/providers/hashicorp/local/latest/docs/resources/file


In the main stack, if you want to use the output of a module
EG:


```
resource "aws ebs" "main" {
    instance = module.anyName.<varible_name>
}
```