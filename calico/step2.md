# Setup k8s with kubeadm


set calico config



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

   curl https://docs.projectcalico.org/v3.9/manifests/calico.yaml -O


   lets look at the bridges created on this node
   `brctl show`{{execute}}

   we can even see the mac address seen on the weave bridge
   `brctl showmacs weave`{{execute}}