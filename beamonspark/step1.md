# Install spark

Lets update Ubuntu first:

`sudo apt-get update`{{execute}}

For full functionality, spark needs java 8

`java -version`{{execute}}

We'll also need python 3:
`python3 -V`{{execute}}

and update it:
`pip3 install --upgrade pip`{{execute}}


Download Spark (https://spark.apache.org/downloads.html):
`curl -O https://downloads.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz`{{execute}}


Extract it:
`tar -xvf spark-3.2.1-bin-hadoop3.2.tgz`{{execute}}

And set it up for execution:
`mv spark-3.2.1-bin-hadoop3.2  /usr/local/spark`{{execute}} 

wip REMOVE THIS LINE sudo ln -s /usr/local/spark-2.4.4-bin-hadoop2.7/ /usr/local/spark   # create link

`export SPARK_HOME=/usr/local/spark`{{execute}}

`export PATH=$PATH:$SPARK_HOME/bin`{{execute}}

. ~/.profile  WIP remove

WIP: java_home has bin on the end, and the error msg has bin/bin, figure on why, below is  a temp fix
check JAVA
`echo $JAVA_HOME`{{execute}}
should equal
`JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre`{{execute}}

And finally lets check spark (for scala) is installed and working:
`spark-shell --version`{{execute}} 

and for python:


`pyspark --version`{{execute}}



