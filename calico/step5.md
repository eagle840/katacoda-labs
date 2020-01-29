# Test Calico Network

WIP: SHOULD WE DO A LITTLE TCPDUMP to look at the pod traffic on the hosts?

Lets remove the taint on the master so it can run pods.
`k taint node master node-role.kubernetes.io/master-`{{execute}}

And deploy a simple nginx deployment 
`k run http --image=nginx --replicas=2`{{execute}}

Take a quick look at the Ip's on the pods on node01 and master
`k get pods -o wide`{{execute}}

Lets pull a couple of troubleshooting images

WIP: use One of the below (busybox?)
`docker pull busybox`{{execute}}
`docker pull nicolaka/netshoot`{{execute}}

ON BOTH TERMINALS

run busybox on host and docker bridge and in k8s pod?, test ping and dns, and server(http?)

`docker run -it --net host busybox`{{execute}}
`docker run -it --net host nicolaka/netshoot`{{execute}}

test ping and dns with these


RESOURCES:
https://schoolofdevops.github.io/zero-to-docker/troubleshooting-toolkit/
https://github.com/nicolaka/netshoot
   