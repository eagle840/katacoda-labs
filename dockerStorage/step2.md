# Volume mounting

In this option a docker volume is created.

docker volume -h

You can create the volume 1st:

docker volume create data_volume

and a volume is created in /var/lib/docker/volumes/data_volume

(in windows:   

-v datavolume:C:\shareddata )

you can then mount that volume to a container:

docker run -v data_volume:/var/lib/mysql   mysql

OR

if you don't have a volume created, docker will create a new one for you.

docker run -v data_volume2:/var/lib/mysql mysql