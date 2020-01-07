Head over to 
https://spark.apache.org/docs/latest/quick-start.html
and well do the scala demo's

You should now see: scala>
[need a refresher on scala?, try leanxinyminutes.com](https://learnxinyminutes.com/docs/scala/)

Let's check out the help function:

`:help`{{execute}}

And do so basic Scala operations.

`val textFile = spark.read.textFile("/usr/local/spark/README.md")`{{execute}}

`textFile.count()`{{execute}}

wip remove line `textFile.count() // Number of items in this Dataset`{{execute}}`

`textFile.first()`{{execute}} // First item in this Dataset

`val linesWithSpark = textFile.filter(line => line.contains("Spark"))`{{execute}}

`textFile.filter(line => line.contains("Spark")).count()`{{execute}} // How many lines contain "Spark"?

#STEP 3 - RDDs and Sparkcontent

In the last section we used a simple data-set, a readme time (just a set of lines, could have been a csv)

What  Spark is know for is RDD's. RDD's have TRANSFORMS and OPERATIONS. Transformations are 