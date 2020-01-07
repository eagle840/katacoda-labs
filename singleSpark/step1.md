# Install spark and tools
WIP: add a 4 session to install juypter and remove it from this section


Lets update Ubuntu first:
`apt install updates -y`{{execute}}

For full functionality, spark needs java 8

`java -version`{{execute}}

We'll also need python 3
`python3 -V`{{execute}}

wip   pip update
`pip3 install --upgrade pip`{{execute}}

wip `python -m pip install findspark`{{execute}}
or `pip3 install findspark`{{execute}}

`pip install jupyterlab`{{execute}}
wip: appears to be running on localhost:4040 only, change to allow internet
`jupyter lab` or  notebook

lets start jupyter with the --ip option, since the default it only for localhost
`jupyter lab --allow-root --ip=0.0.0.0`{{execute}}
wip: cmd automatically opens a browser (lync) find option to this


after starting it'll give you a token to log in with

- starts on port 8888

Download Spark:
`curl -O http://apache.mirrors.nublue.co.uk/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz`{{execute}}
OR grab the url from https://spark.apache.org/downloads.html
USING  release: 2.4
      package 2.7
FOLLOW the url link and select a http (ie non ssl) resource


`tar -xvf spark-2.4.4-bin-hadoop2.7.tgz`{{execute}}
(OR the correct version number)



`mv spark-2.4.4-bin-hadoop2.7 /usr/local/spark`{{execute}} # should /spark  not spark-2.4.4.....

wip REMOVE THIS LINE sudo ln -s /usr/local/spark-2.4.4-bin-hadoop2.7/ /usr/local/spark   # create link

`export SPARK_HOME=/usr/local/spark`{{execute}}

`export PATH=$PATH:$SPARK_HOME/bin`{{execute}}

. ~/.profile  WIP

WIP: java_home has bin on the end, and the error msg has bin/bin, figure on why, below is  a temp fix
check JAVA
`echo $JAVA_HOME`{{execute}}
shoud equal
`JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre`{{execute}}

Lets start the spark shell (scala), with includes the webui (you'll see logs)
`spark-shell`{{execute}}



and connect to the ui
 https://[[HOST_SUBDOMAIN]]-4040-[[KATACODA_HOST]].environments.katacoda.com
