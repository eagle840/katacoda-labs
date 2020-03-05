# install tensorflow


## check k8s

`kubectl cluster-info`{{execute}}



## install updates

'sudo apt update'



## install helm

`curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3`{{execute}}

`chmod 700 get_helm.sh`{{execute}}

`./get_helm.sh`{{execute}}


`helm repo add stable https://kubernetes-charts.storage.googleapis.com/`{{execute}}

`helm repo update`{{execute}}

## install tensorflow through k8s

`helm install stable/distributed-tensorflow --version 0.1.3 --generate-name`{{execute}}

see 'https://hub.helm.sh/charts/stable/distributed-tensorflow' for updated versions

Now wait until all the pods show ready (1/1)


