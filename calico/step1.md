# PRE-SETUP

This scenario is presently in the design process, things may not work

Step 1a: setp a k8s cluster with kubeadm - this will take a minute
in this case we will be setting the pod network to a custom cidr since calico is already to use it
Pull images:
`kubeadm config images pull`{execute}
`kubeadm init --pod-network-cidr 192.168.0.0/16`{{execute}}

After the install on the master is compleat, copy the cmd to init a second computer and paste/exe in the other computer

We'll need the generated config file in the std kubectl config file

`mkdir $HOME/.kube`{{execute}}

`cp /etc/kubernetes/admin.conf $HOME/.kube/config`{{execute}}

and config it's working.

The second node should have finished by now, lets check

`k get nodes --all-namespaces`{{execute}}
You'll see it's not totally ready since we don't have a network solution working.

And lets see what control plane pods are runnning:
`k get pods --all-namespaces`{{execute}}

Your'll notice that the dns pods are waiting for a network to come up
and there are no networking pods running (eg weave-net)

