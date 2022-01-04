Stateful sets require dynamic provisioning to use volumes,  however in this scenario will be using NFS to get around this


Run Ubuntu updates:

`apt-get update -y`{{execute}}

Check k8s is running

`kubectl cluster-info`{{execute}}


# install helm Maually

install helm3  (from https://github.com/helm/helm/releases)

`wget https://get.helm.sh/helm-v3.7.1-linux-amd64.tar.gz`{{execute}}   

`tar -zxvf helm-v3.7.1-linux-amd64.tar.gz`{{execute}}

`mv linux-amd64/helm /usr/local/bin/helm`{{execute}}

`helm version`{{execute}}

# by script

`curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3`{{execute}}

`chmod 700 get_helm.sh`{{execute}}

`./get_helm.sh`{{execute}}




`helm repo add metrics-server https://kubernetes-sigs.github.io/metrics-server/`

```
helm install metrics-server metrics-server/metrics-server \
  --version=4.2.2 \
  --namespace kube-system \
  --set apiService.create=true \
  --set extraArgs.kubelet-insecure-tls=true \
  --set extraArgs.kubelet-preferred-address-types=InternalIP
``` 

search the repo (all repos that have been added), note each has a chart version and an app version

`helm search repo`{{execute}}


`helm repo add bitnami https://charts.bitnami.com/bitnami`{{execute}}   

`helm search repo`{{execute}}

` 
helm install metrics-server bitnami/metrics-server \
  --version=4.2.2 \
  --namespace kube-system \
  --set apiService.create=true \
  --set extraArgs.kubelet-insecure-tls=true \
  --set extraArgs.kubelet-preferred-address-types=InternalIP
` {{execute}}

let check it's installed, since it's installed in the kube-system namespace, we have to add the --namespace argument

`helm list --namespace kube-system`{{execute}}

`helm get notes metrics-server --namespace kube-system`{{execute}}

and lets check what values have been used:

`helm get values metrics-server --namespace kube-system`{{execute}}

Lets check the endpoint is up

`kubectl get --raw /apis/metrics.k8s.io/v1beta1/nodes | jq`{{execute}}

and check the top command (will take a couple of minutes to set getting metrics)

`kubectl top node`{{execute}}

# check layout of helm chart

The following gets the users supplied values:

`helm get values metrics-server -n kube-system`{{execute}}

The following get all the values:

`helm get values metrics-server -n kube-system --all`{{execute}}

To get a pervious release, you can use `--revision <release number>`

`helm pull bitnami/metrics-server`{{execute}}

`tar -zxvf metrics-server-5.10.11.tgz`{{execute}}

`tree metrics-server`{{execute}}




# setup docker images

Create a custom Dockerfile


`nano Dockerfile`{{execute}}

```
FROM php:5-apache
COPY index.php /var/www/html/index.php
RUN chmod a+rx index.php
```

create the index.php file

`nano index.php`{{execute}}
```
<?php
  $x = 0.0001;
  for ($i = 0; $i <= 1000000; $i++) {
    $x += sqrt($x);
  }
  echo "OK!";
?>
```

build the docker image

`docker build -t php-apache .`{{execute}}

Deploy that image into K8S:

`mkdir application`{{execute}}   

`nano application/php-apache.yaml`{{execute}}

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: php-apache
spec:
  selector:
    matchLabels:
      run: php-apache
  replicas: 1
  template:
    metadata:
      labels:
        run: php-apache
    spec:
      containers:
      - name: php-apache
        image: k8s.gcr.io/hpa-example
        ports:
        - containerPort: 80
        resources:
          limits:
            cpu: 500m
          requests:
            cpu: 200m
---
apiVersion: v1
kind: Service
metadata:
  name: php-apache
  labels:
    run: php-apache
spec:
  ports:
  - port: 80
  selector:
    run: php-apache
```



Apply the application in K8S:

`kubectl apply -f https://k8s.io/examples/application/php-apache.yaml`{{execute}}

check the application has been started

`kubectl get pods`{{execute}}





Create the HPA.
`kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10`{{execute}}



`kubectl get hpa`{{execute}}

