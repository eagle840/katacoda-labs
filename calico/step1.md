# PRE-SETUP

This scenario is presently in the design process, things may not work

Setup the k8s cluster with kubeadm - this will take a minute
in this case we will be setting the pod network to a custom cidr since calico is already to use it:

`kubeadm config images pull`{{execute}}  # used for troubleshooting at this time
`kubeadm init --pod-network-cidr 192.168.0.0/16`{{execute}}

After kubeadmin completes we need to complete two other process', copy the config to the ~/.kube file and run the join command on the second node.


You'll see the join command at the end off the kubeadm init, copy that and paste it into the second node in the bottom terminal.

To config the config file over just  look a little further up in the kubeadm init, or just copy and paste this into the top terminal.

```
mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config
```{{copy}}



Lets check the nodes:
`k get nodes`{{execute}}
You'll see it's not totally ready since we don't have a network solution working.

And lets see what control plane pods are runnning:
`k get pods --all-namespaces`{{execute}}
Wait a minute or two, you should see all 8 pods up and running.



