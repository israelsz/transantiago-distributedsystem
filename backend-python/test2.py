import pyspark
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql import functions as F
import json



conf = pyspark.SparkConf().set("spark.jars.packages",
"org.mongodb.spark:mongo-spark-connector_2.12:3.0.1",
    ).setMaster("local").setAppName("SPARK").setAll([
    ("spark.driver.memory", "3g"),
    ("spark.executor.memory", "4g")
    ])

sc = SparkContext(conf = conf)
sqlC = SQLContext(sc)

comments = sqlC.read.format("com.mongodb.spark.sql.DefaultSource").option("spark.mongodb.input.uri",
                                                                      "mongodb://144.22.44.98:8008/RED.PARADEROS").load()
comments.createOrReplaceTempView("PARADEROS")






comments = sqlC.sql(
    "SELECT colorMasRepetido, COUNT(colorMasRepetido) AS cantidad FROM PARADEROS GROUP BY colorMasRepetido ORDER BY cantidad DESC")

# Convert the DataFrame to a JSON array
json_array = comments.toJSON().collect()
  
response = []
for document in json_array:
    json_object =json.loads(document)
    response.append(json_object)
    print(json_object)