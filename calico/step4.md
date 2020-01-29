# review CNI settings

Lets look at the cni config config

`ls /etc/cni/net.d`{{execute}}

now we have files in here, their names assocoated with binaries in the dir `/opt/cni/bin folder` 

`cat /etc/cni/net.d/10-calico.conflist`{{execute}}

`ls /opt/cni/bin`{{execute}}

Since kubelets run on all nodes, you can run the same commands on the lower terminal and get the same results.


`ls /etc/cni/net.d`{{execute HOST2}}

`cat /etc/cni/net.d/10-calico.conflist`{{execute HOST2}}

`ls /opt/cni/bin`{{execute HOST2}}

Lets load up busyboxx3 or netshoot?



Look at the pod bridge IPs, IPAM on cluster/pods
Can use the cni plugin: "host-host" and "DHCP"
The selected one you'll find in `/etc/cnu/net.d/`  under IPAM type:

`cat /etc/cni/net.d`{{execute}}

(weave gives out 10.32.0.0/12 split between nodes)