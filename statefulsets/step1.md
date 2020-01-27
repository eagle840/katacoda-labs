Stateful sets require dynamic provisioning to use volumes,  however in this scenario will be using NFS to get around this


Run Ubuntu updates:

`apt-get update`{{execute}}

Install nfs

`apt install nfs-kernel-server --fix-missing`{{execute}}

`systemctl enable nfs-server`{{execute}}

`systemctl start nfs-server`{{execute}}

`systemctl status nfs-kernel-server`{{execute}} #delete?


Setup some share folders:

`mkdir -p /srv/nfs/kubedata`
`mkdir /srv/nfs/kubedata/{pv0,pv1,pv2,pv3,pv4}`
`chmod -R 777 /srv/nfs`

Update the nfs share configuration:

`echo "/srv/nfs/kubedata    *(rw,sync,no_subtree_check,insecure)" >> /etc/exports`
`exportfs -rav`
`exportfs -v`
`showmount -e`

Take a just check of the server is up and running   111 2049 tcp&udp
`netstat -tlp`

`ip addr | grep ens3`{{execute}}



## TEST
Connect to node01
`ssh node01`
mount the nfs share
`mount -t nfs /<ip>:/src/nfs/kubedata  /mnt`

`ls /mnt  # show see pv0->4`
`umount /mnt`