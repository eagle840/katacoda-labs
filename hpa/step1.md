Stateful sets require dynamic provisioning to use volumes,  however in this scenario will be using NFS to get around this


Run Ubuntu updates:

`apt-get update -y`{{execute}}

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

