import findspark
import os
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, ArrayType, StructType, StructField, FloatType, BooleanType
from pyspark.sql.functions import from_json, col, regexp_replace
from pyspark.sql import SQLContext
from pyspark import SparkContext




# Descarga de paquetes
findspark.init()
findspark.add_packages("org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0,org.mongodb.spark:mongo-spark-connector:10.0.1")


MONGO_IP =  "144.22.44.98"
MONGO_PORT = "8008"
MONGO = f"mongodb://{MONGO_IP}:{MONGO_PORT}/RED.PARADEROS"
# Crea una instancia de SparkSession
spark = SparkSession.builder \
    .appName("Kafka Streaming") \
    .config("spark.mongodb.read.connection.uri", MONGO) \
    .config("spark.mongodb.read.database", "RED") \
    .config("spark.mongodb.read.collection", "PARADEROS") \
    .getOrCreate()


sc = SparkContext()
sqlC = SQLContext(sc)
df = spark.read.format("mongodb").option("uri", "mongodb://144.22.44.98/RED.PARADEROS").load()
df.createOrReplaceTempView("PARADEROS")
df = df.sql("SELECT * FROM PARADEROS")
df.show()


