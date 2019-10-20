# Setup Calico network

download yaml
and create deployment


lets look at the cni

The k8s service responcable for networking and containers is the kubelet

lets look at the startup config
/etc/kubernetes/manifest/kubelet


note the lines
--network plugin=cni
--cni-bin-dir=/opt/cni/bin    # contains the availble plugins
--cni-conf-dir=/etc/cni/net.d # contains the conf for plugin to use

Lets look at the bins:


Lets look at the cni config
    net-script
    plugin config

see:
https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/

and:


https://kubernetes.io/docs/concepts/cluster-administration/networking/

itnext has an articule on performance:
https://itnext.io/benchmark-results-of-kubernetes-network-plugins-cni-over-10gbit-s-network-updated-april-2019-4a9886efe9c4


Has an good support matrix:
https://chrislovecnm.com/kubernetes/cni/choosing-a-cni-provider/