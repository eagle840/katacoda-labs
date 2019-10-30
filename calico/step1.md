# PRE-SETUP

This scenario is presently in the design process, things may not work

Setup the k8s cluster with kubeadm - this will take a minute
in this case we will be setting the pod network to a custom cidr since calico is already to use it:

`kubeadm config images pull`{execute}  # used for troubleshooting at this time
`kubeadm init --pod-network-cidr 192.168.0.0/16`{{execute}}

After the install on the master is complete, copy the cmd at the end of the output to init a second node in the bottom terminal.

Scroll up a little more in the top terminal output, and you'll see three lines to setup the kubectl config, starting with mkdir. Run these three cmds in the top terminal.

Lets check the nodes:
`k get nodes`{{execute}}
You'll see it's not totally ready since we don't have a network solution working.

And lets see what control plane pods are runnning:
`k get pods --all-namespaces`{{execute}}
Your'll notice that the dns pods are waiting for a network to come up
and there are no networking pods running (in this case calico)

