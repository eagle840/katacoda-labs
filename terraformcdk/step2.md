# Using Typescript


taken from:   
https://learn.hashicorp.com/tutorials/terraform/cdktf-install

`cd ~`{{execute}}

`mkdir learn-cdktf-docker`{{execute}}

`cd learn-cdktf-docker`{{execute}}

`cdktf init --template=typescript --local`{{execute}}

enter a project name and description

`npm install @cdktf/provider-docker`{{execute}}


enter code block  cdktf.json and the ts scrip
from
https://github.com/hashicorp/terraform-cdk/tree/main/examples/typescript/docker

rm cdktf.json

wget https://raw.githubusercontent.com/hashicorp/terraform-cdk/main/examples/typescript/docker/cdktf.json

rm main.ts
wget https://raw.githubusercontent.com/hashicorp/terraform-cdk/main/examples/typescript/docker/main.ts



`cdktf get`{{execute}}

`cdktf deploy`{{execute}} and approve the deployment

`docker ps`{{execute}}

`cdktf list`{{execute}}

`cdktf destroy`{{execute}}

