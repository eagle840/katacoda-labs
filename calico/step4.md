# review CNI settings

Lets look at the cni config
`ls /etc/cni/net.d`{{execute}}
again, these are the available plugins to use, and the dir /opt/cni/bin will have the assocoated binaries

`cat /etc/cni/net.d/10-calico.conflist`{{execute}}


`ls /opt/cni/bin`{{execute}}

LOOK AT THE LOWER TERMINAL FOR THE CNI settings

remove the taint to along containers on master



Lets load up busyboxx3 or netshoot?

SHOULD WE DO A LITTLE TCPDUMP to look at the pod traffic on the hosts?



Look at the pod bridge IPs, IPAM on cluster/pods
Can use the cni plugin: "host-host" and "DHCP"
The selected one you'll find in /etc/cnu/net.d/  under IPAM type:

(weave gives out 10.32.0.0/12 split between nodes)