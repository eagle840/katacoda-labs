# Confirm keycloak is working

Lets check that the openID connect and OAuth is working.

Open a new terminal tab

And send the following command to get a token.



https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/auth/admin


`export access_token=$(\
    curl -v -X POST http://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/auth/realms/katacoda/protocol/openid-connect/token \
    -H 'content-type: application/x-www-form-urlencoded' \
    -d 'username=testuser&password=test&grant_type=password&client_id=kube-cluster' | jq --raw-output '.access_token')`{{execute}}


THE -d NEEDS TO BE ONE LINE - DELETEME
`curl -v -X POST http://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/auth/realms/master/procotol/openid-connect/token \
-H 'content-type: application/x-www-form-urlencoded' \
-d grant_type=password   \
-d client_id=kube-cluster  \
-d username=testuser \
-d password=test \
| jq -r '.access token'`


DELETEME   
`curl -v -X POST http://localhost:8443/auth/realms/master/procotol/openid-connect/token \
-H 'content-type: application/x-www-form-urlencoded' \
-d grant_type=password   \
-d client_id=kube-cluster  \
-d username=testuser \
-d password=test \
| jq -r '.access token'`


realm settings > general > click on 'endpoints' openid endpoinnt  config     to get config file

curl it with jq


WIP:

To make a secure request, we need to obtain a token from Keycloak. We can use the token endpoint and the credentials of our test user:






Here we store the access_token in an environment variable:

`echo $access_token`{{execute}}   

Optional: if you want you can copy the token to a jwt token decoder like https://www.jsonwebtoken.io/

  
We can now use this token and pass it as a header in our request. The header will have this format:

key : Authorization
value : Bearer + $access_token

`curl -v -X GET \
  http://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/service/secured \
  -H "Authorization: Bearer "$access_token`


Create a client,   root URL -> url on the katacoda service you usually use



You can go into the clients in keycloak , select sessions, and show sessions - and see whom was  asession open











