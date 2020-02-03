# Test the set

Lets take a look and the PV's and PVC's

`k get pv.pvc`{{execute}}


and delete one of the pods, and see it come back and claim the same pv

Lets connect to one of the pods create a  file

`k exec -it nginx-sts-3 -- /bin/sh`{{execute}}

can create a file

`cd /var/wwww; touch vip.html; ls`{{execute}}

exit out of the session

`exit`{{execute}}

Lets delete the pod

`k delete pod nginx-sts-3`{{execute}}

and in a few moments you'll see it recreated with the same pv, pvc