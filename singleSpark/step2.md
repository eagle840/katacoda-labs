Head over to 
https://spark.apache.org/docs/latest/quick-start.html
and well do the scala demo's

You should now see: scala>



`val textFile = spark.read.textFile("README.md")`{{execute}}

`textFile.count()`{{execute}}

`textFile.count() // Number of items in this Dataset`{{execute}}

textFile.first() // First item in this Dataset

val linesWithSpark = textFile.filter(line => line.contains("Spark"))

textFile.filter(line => line.contains("Spark")).count() // How many lines contain "Spark"?
