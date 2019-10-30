# Reiew CNI & k8S settings

One of the things kubeadm doesn't do is setup the pod networking,  in step 3 we'll getup calico,
but lets take a quick look at the present system.

### Check Bridges
Look at the linux bridges on this system

ADD THESE CMDS TO THE LOWER TERMINAL

`brctl show`{{execute}}

and since we're using docker as the Container Runtime
`docker network ls`{{execute}}

`docker network inspect bridge`{{execute}}
Note that under containers, there are no containers listed, and the IPAM settings
Execute the same cmd on the lower terminal, you see the IPAM address range the same.

The first control plane componet to come up is the kubelet, this will be resposible for directly instructing the containers and the local network. And with the cluster network through a network solution like Calico. 

### CNI Config
Lets look at the cni configuration.

the startup config
`cat /var/lib/kubelet/config.yaml`{{execute}}
note the lines
- --network plugin=cni
- --cni-bin-dir=/opt/cni/bin    # contains the availble plugins binaries for below
- --cni-conf-dir=/etc/cni/net.d # contains the conf files for network plugins to use (in the file name)

the kubelet looks for the right script to run on container creation with net.d, which points to the network script to run (netscript.sh with the container)  CHECK THIS STATMENT I think it's wrong


### Kubelet config

Or, look at the running config (which should be the same):
`ps -aux | grep /usr/bin/kubelet`{{execute}}
lets make it easier to read with the sed command:
`ps -aux | grep /usr/bin/kubelet | sed "s/--/\n--/g"`{{execute}}

Lets look at the cni config  ADD THESE CMDS FOR THE LOWER TERMINAL
`ls /etc/cni/net.d`{{execute}}
Since we have no network plugin, nothing should be there
You'll see the plugin to use in the name of he file.

And the binaries (plugs available), more will  be added installing a network solution:
`ls /opt/cni/bin`{{execute}}
    net-script
    plugin config



the CNI plugin will be responable for the IPAM of the pods(containers), we'll see that in the next step

`ll /etc/cni/net.d/`

k8s services and their IPs (clusterIP and Nodeport) are handed out by the api-server (see under Command: kube-apiserver   --service-cluster-ip-range=10.96.0.0/12) and have more to do with kube-proxy.(CHECK)
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

