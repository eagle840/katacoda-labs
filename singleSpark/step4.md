# Install jupyter and run the same python commands

We've already confirmed that we have the correct version of java and python installed, we'll now install `findspark' to help jupyter work with spark and then install that



wip  USE NEXT LINE `python -m pip install findspark`{{execute}}
or `pip3 install findspark`{{execute}}

`pip3 install jupyterlab`{{execute}}


lets start jupyter with the --ip option, since the default it only for localhost:888

`jupyter lab --allow-root --no-browser --ip=0.0.0.0`{{execute}}

You'll need to copy the token outputted from the cmd to login to Jupyterlab. (ctrl-insert, shift-insert)


and connect to the ui

 https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com

 In the left hand side you'll see the spark file we downloaded earlier, and lets open a Notebook.
 You'll see the notebook added to the file list

 WIP: spark cmds not running


in juypter run:
!pip install findspark
!pip install pyspark

import findspark
import pyspark
findspark.init()
sc = pyspark.SparkContext.getOrCreate()


jupyter allows tab completion (although it maybe alittle slow)
sc. {tab} and select  version. and then shift=enter to run that cammond

Enter each command and then press the play button, or shift-enter to exexcute the command.

Read in the text file:

`textFile = spark.read.text("/usr/local/spark/README.md")`

 Number of rows in this DataFrame

`textFile.count() `

First row in this DataFrame

`textFile.first() `

Run a filter and find the lines with Spark in them

`linesWithSpark = textFile.filter(textFile.value.contains("Spark"))`

`textFile.filter(textFile.value.contains("Spark")).count()  # How many lines contain "Spark"?`

## Congrate's - you've finished the lab.
