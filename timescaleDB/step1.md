`docker pull timescale/timescaledb:latest-pg14`

`wget https://timescaledata.blob.core.windows.net/datasets/nyc_data.tar.gz`
  
`docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb:latest-pg14`

`docker ps`

`docker exec -it timescaledb psql -U postgres`

confirm timescale extension is applied:

`\dx`{execute}

for more info on installtion see: https://docs.timescale.com/install/latest/#install-timescaledb

----------------------------

https://docs.timescale.com/timescaledb/latest/tutorials/nyc-taxi-cab/#introduction-to-iot-new-york-city-taxicabs

apt-get update
apt-get install postgresql-client
psql --version

To connection, use the follow syntax:

psql -x "postgres://tsdbadmin:{YOUR_PASSWORD_HERE}@{YOUR_HOSTNAME_HERE}:{YOUR_PORT_HERE}/tsdb?sslmode=require"

psql -x "postgres://tsdbadmin:password@localhost:5432/tsdb?sslmode=require"