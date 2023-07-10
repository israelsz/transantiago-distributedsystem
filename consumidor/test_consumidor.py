import findspark
#from pyspark.sql.functions import col
from pyspark.sql.functions import from_json, col
from pyspark.sql.functions import from_json, col, regexp_replace
from pyspark.sql.functions import avg, stddev, count, min, max
from pyspark.sql.functions import *
from collections import Counter
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, ArrayType, StructType, StructField, FloatType, BooleanType

def countBusesFueraDeServicio(respuestas, servicios):
    #numBusesFueraServicio = servicios.filter(col("respuestaServicio") == "Fuera de horario de operacion para este paradero").count()
    #servicios.show()
    acum = 0
    print(servicios)
    i = 0
    noDisponibles = ""
    for respuesta  in respuestas["respuestaServicio"]:
        if respuesta == "Fuera de horario de operacion para este paradero" or respuesta == "No hay buses que se dirijan al paradero.":
               acum = acum + 1
               noDisponibles = noDisponibles + servicios["servicio"][i]
        i=i+1
    return acum, noDisponibles

def myFunc(x, y):
    print(y)
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
    #x = list((bool, x))
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
        # Obtener el número de buses fuera de servicio
        #numBusesFueraServicio = countBusesFueraDeServicio(df.servicios.item)
        #df_with_buses_fuera_servicio = df.withColumn("numBusesFueraServicio", lit(numBusesFueraServicio))
        respuestasServicio=df.select("servicios.item.respuestaServicio").collect()[0].asDict()
        myUDF = udf(lambda z,x:myFunc(z,x), ArrayType(StringType()))
        df = df.withColumn("microsNoDisponibles", myUDF(col("servicios.item.respuestaServicio"), col("servicios.item.servicio")))
        myUDFcolor = udf(lambda z:myFuncColor(z), StringType())
        df = df.withColumn("colorMasRepetido", myUDFcolor(col("servicios.item.color")))
        #df = df.withColumn("tieneFueraServicio",
        #                          array_contains(col("servicios.item.respuestaServicio"),"Fuera de horario de operacion para este paradero"))
        #df.show()
        df.write \
        .format("mongodb") \
        .mode("append") \
        .save()
        pass

findspark.init()
findspark.add_packages("org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0,org.mongodb.spark:mongo-spark-connector:10.0.1")
# Crea una instancia de SparkSession
spark = SparkSession.builder \
    .appName("Kafka Streaming") \
    .config("spark.mongodb.read.connection.uri", "mongodb://144.22.44.98:8008/RED.PARADEROS") \
    .config("spark.mongodb.read.database", "RED") \
    .config("spark.mongodb.read.collection", "PARADEROS") \
    .config("spark.mongodb.write.connection.uri", "mongodb://144.22.44.98:8008/RED.PARADEROS") \
    .config("spark.mongodb.write.database", "RED") \
    .config("spark.mongodb.write.collection", "PARADEROS") \
    .getOrCreate()

# Configura las propiedades de Kafka
kafka_topic_name = "macrohard"
kafka_bootstrap_servers = "144.22.52.73:9093"

# Lee los datos de Kafka en formato JSON
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic_name) \
    .option("startingOffsets", "earliest") \
    .option("value.encoding", "UTF-8") \
    .load()
# Decodifica el valor del mensaje como UTF-8
#df = df.selectExpr("CAST(value AS STRING)")
#schema = StructType() \
#    .add("paradero", StringType()) \
#    .add("nomett", StringType()) \
#    .add("fechaprediccion", StringType()) \
#    .add("horaprediccion", StringType()) \
#    .add("x", StringType()) \
#    .add("y", StringType()) \

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

#castDf = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")
#castDf = castDf.withColumn("x", regexp_replace(col("x"), ",", ".").cast(FloatType()))
#castDf = castDf.withColumn("y", regexp_replace(col("y"), ",", ".").cast(FloatType()))
df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")
df = df.withColumn("x", regexp_replace(col("x"), ",", ".").cast(FloatType()))
df = df.withColumn("y", regexp_replace(col("y"), ",", ".").cast(FloatType()))


# Define la lógica de procesamiento de los datos
# Puedes realizar transformaciones, filtrados, agregaciones, etc.

# Muestra los datos en la consola
#query = df.writeStream \
#    .outputMode("append") \
#    .format("console") \
#    .start()

# Espera a que se termine la ejecución
#query.awaitTermination()



# Calcular el promedio de la columna "x"
#promedio_x = df.select(avg("x")).first()[0]

# Define la lógica de procesamiento de los datos
# Puedes realizar transformaciones, filtrados, agregaciones, etc.
#df.writeStream.format("mongodb").mode("append").save()
# Muestra los datos en la consola
#query = df.writeStream \
#    .outputMode("append") \
#    .format("console") \
#    .start()
queryToMongo = df.writeStream.foreachBatch(writeToMongo).start()
queryToMongo.awaitTermination()

# Calcular el promedio de la columna "x"
#promedio_x = df.select(avg("x")).first()[0]
# Espera a que se termine la ejecución
#query.awaitTermination()