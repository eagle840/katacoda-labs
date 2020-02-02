Let's confirm K8s is up and running.

`k get nodes`{{execute}}

`k get pods --all-namespaces`{{execute}}

At this point we are using mTLS/certificates to connect to k8s,

Now we'll setup k8s to use our new Identity provider

## step

in keycloak
add a new client 'k8s-cluster`


WIP: fix tls certs between k8s and keycloak



