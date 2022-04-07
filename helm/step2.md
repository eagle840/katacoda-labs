## Install bitnami metrics-server

search the repo (all repos that have been added), note each has a chart version and an app version

`helm search repo`{{execute}} - None found, so lets add one


`helm repo add bitnami https://charts.bitnami.com/bitnami`{{execute}}   

`helm search repo`{{execute}}

We'll install the metrics-server:

`helm install metrics-server bitnami/metrics-server \
  --version=4.2.2 \
  --namespace kube-system \
  --set apiService.create=true \
  --set extraArgs.kubelet-insecure-tls=true \
  --set extraArgs.kubelet-preferred-address-types=InternalIP
`{{execute}}

Lets check the endpoint is up

`kubectl get --raw /apis/metrics.k8s.io/v1beta1/nodes | jq`{{execute}}

And chect the helm chart is installed (-A shows all namespaces)

`helm list -A`{{execute}}



## Check metrics-server

let check it's installed, since it's installed in the kube-system namespace, we have to add the --namespace argument

`helm list --namespace kube-system`{{execute}}

`helm get notes metrics-server --namespace kube-system`{{execute}}

and lets check what values have been used:

`helm get values metrics-server --namespace kube-system`{{execute}}

The following get all the values:

`helm get values metrics-server -n kube-system --all`{{execute}}

To get a pervious release, you can use `--revision <release number>`

## Pull down and exmine the chart

`helm pull bitnami/metrics-server`{{execute}}

`tar -zxvf metrics-server-5.11.*.tgz`{{execute}}

`tree metrics-server`{{execute}}

