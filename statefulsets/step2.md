
There are three main things to configure for a statefulSet, provision the PV's, Setup a headless service and setup a STS


# Setup the PV's

for this lab we'll setup 5 PV's (pv0 -> pv5)
we'll need the IP of the nfs server, which we got in the previous step: NFSIP.

copy below into pvs.yaml

```
apiVersion: v1
kind: PersistentVolume
metadata:
   name: pv-nfs-pvX
   labels:
     type:  local
spec:
   storageClassName:  manual
   capacity:
      storage: 200Mi
   accessModes:
      - ReadWriteOnce
   nfs:
      server: serverIP   # nfs server address
      path: "/srv/nfs/kubedata/pvX"
```

`sed "s/serverIP/$NFSIP/" pvs.yaml`{{execute}}  #WIP arg to change file
for loop 0 to 4, replace pvX




# Setup the Headless service

```
apiVersion: v1
kind: Service
metadata:
   name: nginx-headless
   labels:
      run: nginx-sts-demo
spec:
   ports:
   - port: 80
     name: web
   clusterIP:  None
   selector:
     run:  nginx-sts-demo
```

# Setup application

note the volume claim templete used in this sts, it will setup the volumes

```
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: nginx-sts
spec:
  serviceName: "nginx-headless"
  replicas: 2
  #podManagementPolicy: Parallel
  selector:
    matchLabels:
      run: nginx-sts-demo
  template:
    metadata:
      labels:
        run: nginx-sts-demo
    spec:
      containers:
      - name: nginx
        image: nginx
        volumeMounts:
        - name: www
          mountPath: /var/www/
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      storageClassName: manual
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 100Mi
```


# Old


if you can enabled a storageClass, the following PV's would be automatically created when the app asked for them.

Put these vols on the node01 ???

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