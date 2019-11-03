# review CNI settings

Lets look at the cni config config
`ls /etc/cni/net.d`{{execute}}
now we have files in here, their names assocoated with binaries in the dir /opt/cni/bin folder 

`cat /etc/cni/net.d/10-calico.conflist`{{execute}}

`ls /opt/cni/bin`{{execute}}

Since kubelets run on all nodes, you can run the same commands on the lower terminal and get the same results.

Lets load up busyboxx3 or netshoot?

SHOULD WE DO A LITTLE TCPDUMP to look at the pod traffic on the hosts?

Look at the pod bridge IPs, IPAM on cluster/pods
Can use the cni plugin: "host-host" and "DHCP"
The selected one you'll find in /etc/cnu/net.d/  under IPAM type:

(weave gives out 10.32.0.0/12 split between nodes)