# Setup Calico network

OK, lets install the calico manifest
`curl https://docs.projectcalico.org/v3.9/manifests/calico.yaml -O`{{execute}}

`kubectl apply -f calico.yaml`{{execute}}

or you can just do it directly from the repo with:
`kubectl apply -f https://docs.projectcalico.org/v3.9/manifests/calico.yaml`

And check the pods and daemonsets are up:
`k get pods --all-namespaces`{{execute}}
`k get ds --all-namespaces`{{execute}}




Let's take a look at the logs for the calico pods

`k logs pod/container -n kube-system'
MAKE SURE NS IS CORRECT, nothing of interest in these

`ps -aux | grep calico`{{execute}}


You'll see a deployment has created a pod  ADD JSON for this command
`k describe pod calico-kube-controllers-5d4bc9cd89-4767z -n kube-system`{{execute}}



