# Install spark


Lets update Ubuntu first:
`apt install updates -y`{{execute}}

Download Spark:
`curl -O http://apache.mirrors.nublue.co.uk/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz`{{execute}}
OR grab the url from https://spark.apache.org/downloads.html
USING  release: 2.4
      package 2.7
FOLLOW the url link and select a http (ie non ssl) resource


`tar -xvf spark-2.4.4-bin-hadoop2.7.tgz`{{execute}}
(OR the correct version number)


```
mv spark-2.4.4-bin-hadoop2.7 /usr/local/ # should /spark  not spark-2.4.4.....

sudo ln -s /usr/local/spark-2.4.4-bin-hadoop2.7/ /usr/local/spark   # create link

export SPARK_HOME=/usr/local/spark

export PATH=$PATH:$SPARK_HOME/bin

. ~/.profile
```

check JAVA
`echo $JAVA_HOME`{{execute}}
shoud equal
`JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre`

spark-shell

http://ipaddress:4040