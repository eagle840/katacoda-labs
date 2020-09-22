## Install docker machine


`base=https://github.com/docker/machine/releases/download/v0.16.0 &&
  curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
  sudo mv /tmp/docker-machine /usr/local/bin/docker-machine &&
  chmod +x /usr/local/bin/docker-machine`{{execute HOST2}}

  `IP_ADDRESS=${<ip of host01}`

  `docker-machine create \
    --driver generic \
    --generic-ip-address=$IP_ADDRESS \
    --generic-ssh-user $USERNAME \
    --generic-ssh-key ~/.ssh/$PRIVATE_KEY \
    host01`

Note:

The driver performs a list of tasks on create:

If docker is not running on the host, it is installed automatically.   
It updates the host packages (apt-get update, yum update...).   
It generates certificates to secure the docker daemon.   
If the host uses systemd, it creates /etc/systemd/system/docker.service.d/10-machine.conf   
The docker daemon restarts, thus all running containers are stopped.   
The hostname is updated to fit the machine name.   



