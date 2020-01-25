Stateful sets require dynamic provisioning to use volumes,  however in this scenario will be using NFS to get around this

`apt-get update`{{execute}}

`apt-get install nfs-kernel-server`{{execute}}

`systemctl status nfs-kernel-server`{{execute}}

Take a just check of the server is up and running   111 2049 tcp&udp
`netstat -tlp`

add the following to /etc/exports
`/srv/nfs/kubedata   *(rw,sync,no_subtree_check,insecure)`{{copy}}


`mkdir -p /srv/nfs/kubedata`{{execute}}

`mkdir -p /srv/nfs/kubedata/{pv0,pv1,pv2,pv3,pv4}`{{execute}}
`chmod -R 777 /srv/nfs`{{execute}}

`exportfs -rav`{{execute}}
`exportfs -v`{{execute}}
`showmount -e`{{execute}}

`ip addr | grep ens3`{{execute}}

## TEST
Connect to node01
`ssh node01`
mount the nfs share
`mount -t nfs /<ip>:/src/nfs/kubedata  /mnt`

`ls /mnt  # show see pv0->4`
`umount /mnt`