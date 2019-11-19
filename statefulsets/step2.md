# Setup application

if you can enabled a storageClass, the following PV's would be automatically created when the app asked for them.

apiVersion: v1
kind: PersistentVolume
metadata:
    name: pv-nfs-pv0
    labels:
       type: local
spec:
    storageClassName: manual
    capacity:
       storage: 200Mi
    accessModes:
       - ReadWriteOnce
    nfs:
       server: 172.17.0.48
       path: "/srv/nfs/katadata/pv0

see
https://github.com/justmeandopensource/kubernetes.git
under yamls, 9-sts

Still need to generate a service to get access (int and/or ext)

use k get sts   to view
use k get all 
scale up and down and see watch and changes (need PV's since no dynamic provisioning)
sts on delete takes down highs \# first, stops if a volume problem
    PVC's have to be delelted manually
    Should really scale down to zero   CHECK!
remove PV's and see if data still in NFS,
    recreate PV's, and sts and see if data is still there?
Should you put a simple website up?