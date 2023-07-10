import findspark
import os
from pyspark.sql.functions import from_json, col
from pyspark.sql.functions import from_json, col, regexp_replace
from pyspark.sql.functions import *
from collections import Counter
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, ArrayType, StructType, StructField, FloatType, BooleanType


def myFunc(x, y):
    acum = 0
    j = 0
    noDisponibles = []
    for i in x:
        if (i == "Fuera de horario de operacion para este paradero" or i == "No hay buses que se dirijan al paradero."):
            acum = acum + 1
            noDisponibles.append(y[j])
        j=j+1
    return noDisponibles


def myFuncColor(x):
    nuevaLista = []
    for i in x:
        if i != "" and i != None:
            nuevaLista.append(i.upper())
    contador = Counter(nuevaLista)
    try:
        elemento, ocurrencias = contador.most_common(1)[0]
        return elemento 
    except:
        return "No hay color mas repetido"
    

def writeToMongo(df, batchId):
        myUDF = udf(lambda z,x:myFunc(z,x), ArrayType(StringType()))
        df = df.withColumn("microsNoDisponibles", myUDF(col("servicios.item.respuestaServicio"), col("servicios.item.servicio")))
        myUDFcolor = udf(lambda z:myFuncColor(z), StringType())
        df = df.withColumn("colorMasRepetido", myUDFcolor(col("servicios.item.color")))
        df = df.withColumn("tieneFueraServicio",
                                  array_contains(col("servicios.item.respuestaServicio"),"Fuera de horario de operacion para este paradero"))
        df.write \
        .format("mongodb") \
        .mode("append") \
        .save()
        pass

# Descarga de paquetes
findspark.init()
findspark.add_packages("org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0,org.mongodb.spark:mongo-spark-connector:10.0.1")

MONGO_IP =  os.environ['IP_MONGO']
MONGO_PORT = os.environ["PORT_MONGO"]
MONGO = f"mongodb://{MONGO_IP}:{MONGO_PORT}/RED.PARADEROS"
# Crea una instancia de SparkSession
spark = SparkSession.builder \
    .appName("Kafka Streaming") \
    .config("spark.mongodb.read.connection.uri", MONGO) \
    .config("spark.mongodb.read.database", "RED") \
    .config("spark.mongodb.read.collection", "PARADEROS") \
    .config("spark.mongodb.write.connection.uri", MONGO) \
    .config("spark.mongodb.write.database", "RED") \
    .config("spark.mongodb.write.collection", "PARADEROS") \
    .getOrCreate()

# Configura las propiedades de Kafka
kafka_topic_name =  os.environ['TOPIC']
kafka_ip =  os.environ['IP_KAFKA']
kafka_port =  os.environ['PORT_KAFKA']
kafka_bootstrap_servers = f"{kafka_ip}:{kafka_port}"

# Lee los datos de Kafka en formato JSON
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic_name) \
    .option("startingOffsets", "earliest") \
    .option("value.encoding", "UTF-8") \
    .load()


schema = StructType([
    StructField("fechaprediccion", StringType()),
    StructField("horaprediccion", StringType()),
    StructField("nomett", StringType()),
    StructField("paradero", StringType()),
    StructField("respuestaParadero", StringType()),
    StructField("servicios", StructType([
        StructField("item", ArrayType(StructType([
            StructField("servicio", StringType()),
            StructField("codigorespuesta", StringType()),
            StructField("distanciabus1", StringType()),
            StructField("distanciabus2", StringType()),
            StructField("horaprediccionbus1", StringType()),
            StructField("horaprediccionbus2", StringType()),
            StructField("ppubus1", StringType()),
            StructField("ppubus2", StringType()),
            StructField("respuestaServicio", StringType()),
            StructField("color", StringType()),
            StructField("destino", StringType()),
            StructField("sentido", StringType()),
            StructField("itinerario", BooleanType()),
            StructField("codigo", StringType())
        ])))
    ])),
    StructField("urlLinkPublicidad", StringType()),
    StructField("urlPublicidad", StringType()),
    StructField("x", StringType()),
    StructField("y", StringType())
])


df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")
df = df.withColumn("x", regexp_replace(col("x"), ",", ".").cast(FloatType()))
df = df.withColumn("y", regexp_replace(col("y"), ",", ".").cast(FloatType()))

queryToMongo = df.writeStream.foreachBatch(writeToMongo).start()
queryToMongo.awaitTermination()
