# Setup Calico network

Install the calico manifest
`curl https://docs.projectcalico.org/v3.9/manifests/calico.yaml -O`{{execute}}

`kubectl apply -f calico.yaml`{execute}

or you can just do it directly
'kubectl apply -f https://docs.projectcalico.org/v3.9/manifests/calico.yaml`

`k get pods --all-namespaces`{{execute}}

install the calico ctl
  
     https://docs.projectcalico.org/v3.9/getting-started/calicoctl/install 
  download calicoctl
  chmod
  path

We'll connect to the k8s in the next step
   https://docs.projectcalico.org/v3.9/getting-started/calicoctl/configure/kdd
   


   VERSION TWO

   curl https://docs.projectcalico.org/v3.9/manifests/calico.yaml -O
