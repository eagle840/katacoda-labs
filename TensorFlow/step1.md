# install tensorflow

## install updates

'sudo apt update'



## install helm

`curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3`

`chmod 700 get_helm.sh`

`./get_helm.sh`


`helm repo add stable https://kubernetes-charts.storage.googleapis.com/`

`helm repo update`

## install tensorflow through k8s

`helm install stable/distributed-tensorflow --version 0.1.3`

see 'https://hub.helm.sh/charts/stable/distributed-tensorflow' for updated versions


