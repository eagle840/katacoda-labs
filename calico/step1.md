# PRE-SETUP

This scenario is presently in the design process, things may not work.

WIP: Work In Progress

First lets setup the k8s cluster with kubeadm - this will take a minute -
in this case we will be setting the pod network to a custom cidr since calico is already to use it, and downloading the images before executing the kubeadm init.

`kubeadm config images pull`{{execute}}  
`kubeadm init --pod-network-cidr 192.168.0.0/16`{{execute}}

After kubeadmin completes we need to complete two other process', 
* copy the config to the ~/.kube file and 
* run the join command on the second node.


You'll see the join command at the end off the `kubeadm init` stdout, but  if you scroll up alittle you'll see the commands to setup the config file to have kubectl work with this cluster. Copy that and paste it into the second node in the bottom terminal.

If you run `kubectl get nodes` you should see the master running

Now copy the kubeadmin init command at the end of the stdout on the lower terminal and it will install kubernetes on that node for this cluster.



Now lets check the nodes running on this cluster again, you should see two.:
`k get nodes`{{execute}}
You'll see it's not totally ready since we don't have a network solution working.

And lets see what control plane pods are runnning:
`k get pods --all-namespaces`{{execute}}
Wait a minute or two, you should see all 8 pods up and running.



