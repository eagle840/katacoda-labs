Stateful sets require dynamic provisioning to use volumes,  however in this scenario will be using NFS to get around this


Run Ubuntu updates:

`apt-get update`{{execute}}

Install nfs

`apt install nfs-kernel-server --fix-missing`{{execute}}

`systemctl enable nfs-server`{{execute}}

`systemctl start nfs-server`{{execute}}

`systemctl status nfs-kernel-server`{{execute}} #delete?


Setup some share folders:

`mkdir -p /srv/nfs/kubedata`{{execute}}
`mkdir /srv/nfs/kubedata/{pv0,pv1,pv2,pv3,pv4}`{{execute}}
`chmod -R 777 /srv/nfs`{{execute}}

Update the nfs share configuration:

`echo "/srv/nfs/kubedata    *(rw,sync,no_subtree_check,insecure)" >> /etc/exports`{{execute}}
`exportfs -rav`{{execute}}
`exportfs -v`{{execute}}
`showmount -e`{{execute}}

Take a just check of the server is up and running   111 2049 tcp&udp
`netstat -tlp`{{execute}}

And let's set an env for the nfs server which we'll use in the next steps.
`ip addr | grep ens3`{{execute}}
`NFSIP=$(ip addr show ens3  | awk '$1 == "inet" { print $2 }' | cut -d/ -f1)`{{execute}}


## TEST (WIP)
Connect to node01
`ssh node01`
mount the nfs share
WIP fix following
`ssh root@node01 mount -t nfs $NFSIP:/srv/nfs/kubedata  /mnt`{{execute}}

`ssh root@node01 ls /mnt  # show see pv0->4`{{execute}}
`ssh root@node01 umount /mnt`{{execute}}