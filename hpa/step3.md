# Custom and multiple metrics

Lets get a copy of the HPA yaml

`kubectl get hpa php-apache -o yaml > /tmp/hpa-v2.yaml`{{execute}}

Review the documentation at: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/


=============================== copied from katacode observe  https://www.katacoda.com/courses/kubernetes/kubernetes-observability-basics-by-javajon


Add the Bitnami chart repository for the Helm chart to be installed.

helm repo add bitnami https://charts.bitnami.com/bitnami

Install the chart.

helm install metrics-server bitnami/metrics-server \
  --version=4.2.2 \
  --namespace kube-system \
  --set apiService.create=true \
  --set extraArgs.kubelet-insecure-tls=true \
  --set extraArgs.kubelet-preferred-address-types=InternalIP
This will install the server in the kube-system namespace. It also add a new API endpoint named metrics.k8s.io. In a few moments you should be able to list metrics using the following command:

kubectl get --raw /apis/metrics.k8s.io/v1beta1/nodes | jq

If the metrics are not ready, this message will appear

Error from server (ServiceUnavailable): the server is currently unable to handle the request

Once the metrics are ready, a JSON dump of the metrics will appear. Additional metrics also appears in the top report.

kubectl top node

If the metrics are not ready you may get this message.

Error from server (ServiceUnavaliable): the server is currently unable to handle the request (get nodes.metrics.k8s.io)

or

error: metrics not available yet

However, once the metrics are available the normal message should look similar to this:

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
controlplane   138m         6%     991Mi           52%
node01         79m          3%     575Mi           14%
Pod information can also be observed.

kubectl top pods --all-namespaces






