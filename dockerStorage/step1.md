# Bind mounting - Using Local Volume Drivers

When starting a docker container,

you use -v /data/sql:/var/lib/mysql

where /data/sql  is your local directory   
and /var/lib/mysql is the directory on the container

for windows: `-v c:\data\sql:c:\notsureforsql`

# New option

is the mount command

--mount type=bind, source=/data/sql, target=/var/lib/mysql