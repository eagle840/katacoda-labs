
Lets check that the openID connect and OAuth is working 

curl -X POST https://localhost:8443/auth/realms/master/procotol/openid-connect/token \
-d grant_type=password   \
-d client_id=testclient  \
-d username=admin \
-d password=admin \
| jq -r `.access token`


realm settings > general > click on openid endpoinnt to get config file

curl it with jq



Let's confirm K8s is up and running (in a second terminal).

`k get nodes`{{execute T2}}

`k get pods --all-namespaces`{{execute T2}}

At this point we are using mTLS/certificates to connect to k8s,

Now we'll setup k8s to use our new Identity provider

## step

in keycloak
add a new client 'k8s-cluster`


WIP: fix tls certs between k8s and keycloak

point k8s to openid connect std endpoint discovery service

[k8s authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/)



