### install helm

`curl -LO https://storage.googleapis.com/kubernetes-helm/helm-v2.8.2-linux-amd64.tar.gz
tar -xvf helm-v2.8.2-linux-amd64.tar.gz
mv linux-amd64/helm /usr/local/bin/`{{execute}}

`helm init
helm repo update`{{execute}}

### install spark

see: [spark chart](https://hub.helm.sh/charts/incubator/spark)


`helm repo add incubator https://kubernetes-charts-incubator.storage.googleapis.com`{{execute}}

`helm install incubator/spark --name sparkzep --version 0.1.1 --set Worker.Memory=256Mi`{{execute}}

### Adjust the service types.

The helm chart for this deployment creats 2 ext LB's but we need to change them to Ports

WIP: code for the yaml files into the project

k get svc sparkzep-spark-webui

k delete svc sparkzep-spark-webui

k create -f webui-svc.yaml

and connect to http 32329   to view the spark master status

/* note that the web ui shows 7077, k8s is redirecting this to 32329 and that you can't conect to any node 

WIP: why are the worker nodes showing  1024, it should be 512?



