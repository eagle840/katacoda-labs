# modules

`mkdir modules`{{execute}}

`cd modules`{{execute}}

`mkdir nginxsite`{{execute}}

`cd nginxsite`{{execute}}

A typical module contains:

.
├── LICENSE
├── README.md
├── main.tf
├── variables.tf
├── outputs.tf

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




https://registry.terraform.io/providers/hashicorp/local/latest/docs/resources/file
