# IN PROGRESS 

This scenario is presently in the design process, please do not use.



Kubernetes imposes the following fundamental requirements on any networking implementation (barring any intentional network segmentation policies):

 - pods on a node can communicate with all pods on all nodes without NAT
 - agents on a node (e.g. system daemons, kubelet) can communicate with all pods on that node
Note: For those platforms that support Pods running in the host network (e.g. Linux):

- pods in the host network of a node can communicate with all pods on all nodes without NAT

ADD REVIEW OF CNI
ADD REVIEW OF HOW TO CHECK K8S config for CNI

This scenario follows the instructions as provided in the Calico project:
https://docs.projectcalico.org/v3.9/getting-started/kubernetes/installation/

specifically for: Installing Calico for policy and networking (recommended)

Basic understanding of CNI and kubeadm is expected