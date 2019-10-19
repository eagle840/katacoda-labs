# PRE-SETUP

This scenario is presently in the design process, please do not use

Step 1a: setp a k8s cluster with kubeadm - this will take a minute
in this case we will be setting the pod network to a custom cidr since calico is already to use it
`kubeadm init --pod-network-cidr 192.168.0.0/16`{{execute}}

After the install on the master is compleat, copy the cmd to init a second computer and paste/exe in the other computer

We'll need the generated config file in the std kubectl config file

`mkdir -p $HOME/.kube`{{execute}}
`sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config`{{execute}}
`sudo chown $(id -u):$(id -g) $HOME/.kube/config`{{execute}}

and config it's working.

The second node should have finished by now, lets check

`k get nodes`{{execute}}



VERSION ONE 
download calicoctl 

install the calico ctl
  
     https://docs.projectcalico.org/v3.9/getting-started/calicoctl/install 
  download calicoctl
  chmod
  path

We'll connect to the k8s in the next step
   https://docs.projectcalico.org/v3.9/getting-started/calicoctl/configure/kdd
   


   VERSION TWO

   (https://docs.projectcalico.org/v3.10/getting-started/kubernetes/)[https://docs.projectcalico.org/v3.10/getting-started/kubernetes/]

   `kubectl apply -f https://docs.projectcalico.org/v3.10/manifests/calico.yaml`{{execute}}

   curl https://docs.projectcalico.org/v3.9/manifests/calico.yaml -O