## docker compose

In this step we'll be using docker-compose.

first create a folder to hold your composer files:


`mkdir compose1 && cd compose1`{{execute}}

create the file: docker-compose.yml  and paste the yaml file in.

`nano docker-compose.yml`{{execute}}

(ctrl-insert:copy shift-insert:paste)


```yaml
version: '3'

services:

    mysql-dev:
        image: mysql:8.0.2
        environment:
            MYSQL_ROOT_PASSWORD: 1234
            MYSQL_DATABASE: blogapp
        ports:
           - "3308:3306"
        volumes:
           - "./data:/var/lib/mysql:rw"
```

lets copy across the data folder we created in step 1

**WIP**  the following is breaking the docker compose

`cp -r /root/data/ /root/compose1/data/`{{execute}}

`docker-compose up`{{execute}}

confirm ruuning  
`docker-compose ps`{{execute}}


you can connect to the container in either way:  
`docker exec -it root_mysql-dev_1 /bin/bash`{{execute}}

`docker-compose exec  mysql-dev /bin/bash`{{execute}}


## add service to docker-compose.yml

Add   the following test to the end of the docker-compose file.

`nano docker-compose.yml`{{execute}}

``` yaml
    client:
        image: mysql:8.0.2
        depends_on:
            - mysql-dev
        command: mysql -uroot -p1234 -hmysql-dev blogapp
```

**WIP** the following captures to terminal

`docker-compose up `{{execute}}

note that the client will exit

`docker-compose run --rm client`{{execute}}  

will connect you

`docker-compose ps`{{execute}}

shows a new container running 

Perhaps we need to add another legacy db:

``` yaml
mysql-legacy:
    image: mysql:5.7
    envirnoment:
        MYSQL_ROOT_PASSWORD: 1234
        MYSQL_DATABASE: 2014app
    ports:
    - "3309:3306"
```

lets' check

`docker-compose ps`{{execute}}

`docker-compose exec mysql-legacy mysql -uroot -p1234 2014app`{{execute}}


### adminer

Lets add another service to the yml

``` yaml
    admin:
        image: adminer
        ports:
        - 8080:8080
```

`docker-compose up`{{execute}}

https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com

```
system: mysql
server: compose1_mysql-dev_1   (from docker-compose ps)
un: root
pw: 1234
database: test1
```



## postgres

Lets add a postgres db   url for postgres on docker hub 

```yaml
    postgres1:
        image: postgres
        environment:
            POSTGRES_USER: root
            POSTGRES_PASSWORD: 1234
            POSTGRES_DB: blogapp
```

connect with adminer

connect with cli

`docker-compose exec postgres1 psql -U root -W blogapp`{{execute}}

## connect to mysql and postgres with adminer


