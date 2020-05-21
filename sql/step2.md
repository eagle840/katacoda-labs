# Save And Restore

In this step we'll backup a the databases, remove them and then restore

Lets create a backup folder on the local host

`mkdir backups`{{execute}}

and start mysql in docker, setting up a volume for the database and one for the backup.

Since the sql data is still in the data volume from the last step, we'll be using that as the db. ***WIP*** no its not

`docker run --name some-mysql -v /root/data:/var/lib/mysql -v /root/backups:/backups -e MYSQL_ROOT_PASSWORD=1234 -d mysql`{{execute}}


### backup one db


we'll use the mysqldump command to generate a txt backup file:

Lets connect to the docker container and use the mysqldump to backup the database test1:

`docker exec -it some-mysql bash`{{execute}}

`mysqldump --add-drop-table --password=1234 --databases test1  > /backups/$(/bin/date +\%Y-%m-\%d).sql.bak`{{execute}}

(note: using this script will overwrite the backup if run again over the same day)

***WIP IS DROP-TABLE needed**

### backup all

`mysqldump --all-databases --password=1234  > /backups/fulldump.sql`{{execute}}


Lets go ahead and destroy the container   

`exit`{{execute}}   


`docker exec -it  some-mysql mysql -uroot -p1234 -e "drop database test1"`{{execute}} 

`docker stop some-mysql`{{execute}}

`docker rm some-mysql `{{execute}}

Lets remove the data folder

`rm -r /data/`

## Restore

Startup the docker container:   

`docker run --name some-mysql -v /root/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=1234 -d mysql`{{execute}}

and connect

`docker exec -it some-mysql bash`{{execute}}   

`mysql -uroot -p1234 [database name] < <backupname>.sql`

**WIP** correctly mount the volume for restore

`mysql -uroot -p < fulldump.sql`


# SETUP AUTO BACKUP

In this part we'll setup a cron job to automatically run backups

so we don't have to be prompted everytime we run a backup, we'll create a .my.cnf file with the un and pw

store mysql root password in /root/.my.cnf   (chmod 600 .my.cnf)  
**WIP*** needs to go into container  
copy and paste into  .my.conf  

'''yaml
[client]
user=root
password=1234
'''
and allow only root  
`chmod 600 .my.cnf`{{execute}}

### schedule it with crontab

`nano /etc/crontab`

(8:06)


## Reset password

check mysql docs to add section

## remove the container

`docker stop some-mysql`{{execute}}

`docker rm some-mysql `{{execute}}

