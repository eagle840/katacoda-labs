Now we'll the Python demo.

exit scale with `:quit`

and run 
`pyspark`{{execute}}

`textFile = spark.read.text("/usr/local/spark/README.md")`{{execute}}

`textFile.count()  # Number of rows in this DataFrame`{{execute}}

`textFile.first()  # First row in this DataFrame`{{execute}}

`linesWithSpark = textFile.filter(textFile.value.contains("Spark"))`{{execute}}

`textFile.filter(textFile.value.contains("Spark")).count()  # How many lines contain "Spark"?`{{execute}}
