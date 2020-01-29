# Review CNI & k8S settings

One of the things kubeadm doesn't do is setup the pod networking,  in step 3 we'll setup calico,
but lets take a quick look at the present system.

### Check Bridges
Let's take a look at the linux bridges on this system



`brctl show`{{execute}}

and on the second host:

`brctl show`{{execute HOST2}}

and since we're using docker as the Container Runtime lets look at the configuration:

`docker network ls`{{execute}}

`docker network inspect bridge`{{execute}}

and on the second host:

`docker network ls`{{execute HOST2}}

Note that under containers, there are no containers listed, and the IPAM settings
Execute the same cmd on the lower terminal, you see the IPAM address range the same.

The first control plane componet to come up is the kubelet, this will be resposible for directly instructing the containers and the local network. and for the cluster network through a network solution like Calico. 

### Kubelet Configuration

the startup kubelet config

`cat /var/lib/kubelet/config.yaml`{{execute}}


Or, look at the running config (which should be the same):

`ps -aux | grep /usr/bin/kubelet`{{execute}}

lets make it easier to read with the sed command:

`ps -aux | grep /usr/bin/kubelet | sed "s/--/\n--/g"`{{execute}}

note the lines
```
- --network plugin=cni
- --cni-bin-dir=/opt/cni/bin    # contains the availble plugins binaries for below
- --cni-conf-dir=/etc/cni/net.d # contains the conf files for network plugins to use (in the file name)
```

the kubelet looks for the right script to run on container creation with net.d, which points to the network script to run (netscript.sh with the container)  CHECK THIS STATEMENT I think it's wrong


Lets look at the cni config  ADD THESE CMDS FOR THE LOWER TERMINAL

`ls /etc/cni/net.d`{{execute}}

Since we have no network plugin, nothing should be there
You'll see the plugin to use in the name of he file when its installed.

And the binaries (plugs available), you'll see more when we have added a network solution:
`ls /opt/cni/bin`{{execute}}
    net-script
    plugin config


k8s services and their IPs (clusterIP and Nodeport) are handed out by the api-server, not the kubelet. However the kube-proxy on each node is responcable for handling their traffic. (see under Command: kube-apiserver   --service-cluster-ip-range=10.96.0.0/12).
`k describe pod kube-apiserver-master  -n kube-system`{{execute}} 

Lets look the the command and args:
`k get pod kube-apiserver-master  -n kube-system -o json | jq .spec.containers[0].command`{{excute}}

when creating your k8 cluster from scratch, it's important that you don't conflict these while the CNI IPAM setup.

## spin up some pods without a network

`k run nettools --image=nicolaka/netshoot --replicas 2 -- sleep 3600`{{execute}}
and take a look at there ip address'
`k get pods -o wide`{{execute}}
APPEARS TO BE WAY OUT OF DATE - PERHAPS USE BUSYBOX?




