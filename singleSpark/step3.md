# Run python
Now we'll the Python demo.

exit scala with `:quit`{{execute}}

and run 

`pyspark`{{execute}}

In order to quit pyspark: `quit()`

We'll run the similar commands in step 2, but in python:

`textFile = spark.read.text("/usr/local/spark/README.md")`{{execute}}

`textFile.count()  # Number of rows in this DataFrame`{{execute}}

`textFile.first()  # First row in this DataFrame`{{execute}}

`linesWithSpark = textFile.filter(textFile.value.contains("Spark"))`{{execute}}

`textFile.filter(textFile.value.contains("Spark")).count()  # How many lines contain "Spark"?`{{execute}}
