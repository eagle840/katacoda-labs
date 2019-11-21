Stateful sets require dynamic provisioning to use volumes,  however in this scenario will be using NFS to get around this

`apt-get update`{{execute}}

`apt-get install nfs-kernel-server`{{execute}}

`systemctl status nfs-kernel-server`{{execute}}

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
ssh to node01
mount -t nfs /<ip>:/src/nfs/kubedata  /mnt
ls /mnt  # show see pv0->4
umount /mnt