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
    "SELECT microsNoDisponibles FROM PARADEROS")

comments_exploded = comments.select(F.explode("microsNoDisponibles").alias("microsNoDisponibles"))
comments_exploded.createOrReplaceTempView("PARADEROS_B")
comments_exploded = sqlC.sql(
    "SELECT microsNoDisponibles, COUNT(microsNoDisponibles) AS cantidad FROM PARADEROS_B GROUP BY microsNoDisponibles ORDER BY cantidad DESC")
comments_exploded.show()

# Convert the DataFrame to a JSON array
json_array = comments_exploded.toJSON().collect()
  
response = []
for document in json_array:
    json_object =json.loads(document)
    json_object["micro"] = json_object.pop("microsNoDisponibles")
    response.append(json_object)
    print(json_object[0])

"""
comments = sqlC.sql(
    "SELECT colorMasRepetido, COUNT(colorMasRepetido) AS cantidad FROM PARADEROS GROUP BY colorMasRepetido ORDER BY cantidad DESC")
comments.show()
+--------------------+--------+                                                 
|    colorMasRepetido|cantidad|
+--------------------+--------+
|             #ED1C24|      16|
|             #00A77E|     218|
|             #FFD400|      46|
|             #0077BB|     213|
|             #0093B3|     104|
|             #CF152D|     282|
|             #F7941D|      67|
|No hay color mas ...|       4|
+--------------------+--------+
"""