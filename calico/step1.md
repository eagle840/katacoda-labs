# PRE-SETUP

This scenario is presently in the design process, please do not use

Step 1a: setp a k8s cluster with kubeadm - this will take a minute
in this case we will be setting the pod network to a custom cidr since calico is already to use it
`kubeadm init --pod-network-cidr 192.168.0.0/16`{{execute}}

After the install on the master is compleat, copy the cmd to init a second computer and paste/exe in the other computer

We'll need the generated config file in the std kubectl config file

`mkdir $HOME/.kube`{{execute}}

`cp /etc/kubernetes/admin.conf $HOME/.kube/config`{{execute}}

and config it's working.

The second node should have finished by now, lets check

`k get nodes --all-namespaces`{{execute}}

Your'll notice that the dns pods are waiting for a network to come up

Since the kubelet is one of the first components to come up and is responcable for starting all pods, lets look at the startup
`ps -aux | grep /usr/bin/kubelet`{{execute}}
lets make it easier to read
`ps -aux | grep /usr/bin/kubelet | sed 's/--/\n--/g'`{{execute}}

the CNI plugin will be responable for the IPAM of the pods(containers), we'll see that in the next step

k8s services and their IPs (clusterIP and Nodeport) are handed out by the api-server (--service-cluster-ip-range=10.96.0.0/12)
`k describe pod kube-apiserver-master  -n kube-system`{{execute}} 

when creating your k8 cluster from scratch, it's important that you don't conflict these while the CNI IPAM setup.