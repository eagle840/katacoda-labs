# Other Volume Drivers

Other options inc:

- Azure File Storage
- Convoy
- Flocker
- GlusterFS
- NetApp
- RexRay
- Portworx
- VMware vSphere Storage
- DigitalOCean Block Storage
- GCE-Docker

To use:

docker run -it \
  --name mysql
  --volume-driver rexray/ebs
  --mount src=ebs-vol, target=/var/lib/mysql
  mysql