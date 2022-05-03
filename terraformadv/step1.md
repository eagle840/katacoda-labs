# initial setup


## install terraform
`apt upgrade`{{execute}}   # takes too long!

`sudo apt update`{{execute}}    

`curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -`{{execute}}    

`apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"`{{execute}}  


`apt install terraform`{{execute}}    

`terraform version`{{execute}}    

  

`terraform -install-autocomplete`{{execute}}    

`exec bash`{{execute}}

# 

`k cluster-info`{{execute}}

`python3 -V`{{execute}}

# install helm

`curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3`{{execute}}

`chmod 700 get_helm.sh`{{execute}}

`./get_helm.sh`{{execute}}`curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3`{{execute}}

`chmod 700 get_helm.sh`{{execute}}

`./get_helm.sh`{{execute}}

`helm version`{{execute}}

# install a demo chart (nginx)

`helm create nginx`{{execute}}

`helm install new-chart nginx/ --values nginx/values.yaml`{{execute}}

`helm list -A`{{execute}}

`k get deploy`{{execute}}