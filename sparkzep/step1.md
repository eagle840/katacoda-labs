### install helm

`launch.sh`{{execute}}

Lets first allow the master node be able to run pods:

`k taint node controlplane node-role.kubernetes.io/master:NoSchedule-`{{execute}}


And install helm 3

`curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3`{{execute}}   

`chmod 700 get_helm.sh`{{execute}} 

`./get_helm.sh`{{execute}}   


`helm version`{{execute}}

### install spark



`helm repo add bitnami https://charts.bitnami.com/bitnami`{{execute}}

`helm install sparkzep bitnami/spark`{{execute}}

It'll take a few minute to spin up the cluster. run to check that the pods are all running (status = running).

`k get pods`{{execute}}

`helm status sparkzep`{{execute}}


### Adjust the service types.

The helm chart for this deployment creates 2 ext LB's but we need to change them to NodePorts


`k get svc sparkzep-spark-webui`{{execute}}

`k delete svc sparkzep-spark-webui`{{execute}}

`k create -f webui-svc.yaml`{{execute}}

and connect to http 32329   to view the spark master status (takes a minute or two to come up)

https://[[HOST_SUBDOMAIN]]-32329-[[KATACODA_HOST]].environments.katacoda.com

* note that the web ui shows 7077, k8s is redirecting this to 32329 and that you can't conect to any node 

WIP: why are the worker nodes showing  1024, it should be 512?

And lets adjust the zepplin server to run with katacoda

`k get svc sparkzep-zeppelin-contro`{{execute}}

`k delete svc sparkzep-zeppelin-contro`{{execute}}

`k create -f zeppelin-svc.yaml`{{execute}}

https://[[HOST_SUBDOMAIN]]-30466-[[KATACODA_HOST]].environments.katacoda.com





