### install helm

`curl -LO https://storage.googleapis.com/kubernetes-helm/helm-v2.8.2-linux-amd64.tar.gz
tar -xvf helm-v2.8.2-linux-amd64.tar.gz
mv linux-amd64/helm /usr/local/bin/`{{execute}}

`helm init
helm repo update`{{execute}}

### install spark

see: [spark chart](https://hub.helm.sh/charts/incubator/spark)


`helm repo add incubator https://kubernetes-charts-incubator.storage.googleapis.com`{{execute}}

helm install incubator/spark --name sparkzep --version 0.1.1 --set Worker.Memory=256Mi

### Adjust the service types.

The helm chart for this deployment creats 2 ext LB's but we need to change them to Ports