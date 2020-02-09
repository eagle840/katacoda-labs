
Lets check that the openID connect and OAuth is working 

curl -X POST https://localhost:8443/auth/realms/master/procotol/openid-connect/token \
-d grant_type=password   \
-d client_id=testclient  \
-d username=admin \
-d password=admin \
| jq -r `.access token`


realm settings > general > click on 'endpoints' openid endpoinnt  config     to get config file

curl it with jq


WIP:

To make a secure request, we need to obtain a token from Keycloak. We can use the token endpoint and the credentials of our test user:

export access_token=$(\
    curl -X POST http://2886795272-8443-host08nc.environments.katacoda.com/auth/realms/katacoda/protocol/openid-connect/token \
    -H 'content-type: application/x-www-form-urlencoded' \
    -d 'username=test&password=test&grant_type=password&client_id=katacoda-cli' | jq --raw-output '.access_token' \
 )

Here we store the access_token in an environment variable:

echo $access_token

Make a secure request
We can now use this token and pass it as a header in our request. The header will have this format:

key : Authorization
value : Bearer + $access_token
curl -v -X GET \
  http://2886795272-3000-host08nc.environments.katacoda.com/service/secured \
  -H "Authorization: Bearer "$access_token


Create a client,   root URL -> url on the katacoda service you usually use



You can go into the clients in keycloak , select sessions, and show sessions - and see whom was  asession open








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



