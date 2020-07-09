# k8s setup

![idp](https://d33wubrfki0l68.cloudfront.net/d65bee40cabcf886c89d1015334555540d38f12e/c6a46/images/docs/admin/k8s_oidc_login.svg)

[k8s authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/)


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
