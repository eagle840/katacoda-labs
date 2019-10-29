# Reiew CNI & k8S settings

Look at the bridges on this system

`brctl show`{{execute}}
and 
`docker network ls`{{execute}}
`docker network inspect docker0`{{execute}}

The first control plane componet to come up is the kubelet, this will be resposible for directly instructing the containers and the local network. And with the cluster network through a network solution like Calico 

Lets look at the cni configuration.


lets look at the startup config
`cat var/lib/kubelet/config.yaml`{{execute}}
note the lines
--network plugin=cni
--cni-bin-dir=/opt/cni/bin    # contains the availble plugins
--cni-conf-dir=/etc/cni/net.d # contains the conf for plugin to use
Or, look at the running config:
`ps -aux | grep /usr/bin/kubelet | sed "s/--/\n--/g"`{{execute}}


Lets look at the bins:


Lets look at the cni config
    net-script
    plugin config

Since the kubelet is one of the first components to come up and is responsible for starting all pods, lets look at the startup
`ps -aux | grep /usr/bin/kubelet`{{execute}}
lets make it easier to read
`ps -aux | grep /usr/bin/kubelet | sed 's/--/\n--/g'`{{execute}}

the CNI plugin will be responable for the IPAM of the pods(containers), we'll see that in the next step

`ll /etc/cni/net.d/`

k8s services and their IPs (clusterIP and Nodeport) are handed out by the api-server (--service-cluster-ip-range=10.96.0.0/12)
`k describe pod kube-apiserver-master  -n kube-system`{{execute}} 

when creating your k8 cluster from scratch, it's important that you don't conflict these while the CNI IPAM setup.



RESOURCES
see:
https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/

https://kubernetes.io/docs/concepts/cluster-administration/networking/

itnext has an articule on performance:
https://itnext.io/benchmark-results-of-kubernetes-network-plugins-cni-over-10gbit-s-network-updated-april-2019-4a9886efe9c4


Has an good support matrix:
https://chrislovecnm.com/kubernetes/cni/choosing-a-cni-provider/

