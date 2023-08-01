from flask import Flask, jsonify
import pyspark
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql import functions as F
import json


def colorPopularSpark():
    commentsColor = sqlC.sql(
    "SELECT colorMasRepetido, COUNT(colorMasRepetido) AS cantidad FROM PARADEROS GROUP BY colorMasRepetido ORDER BY cantidad DESC")
    # Convert the DataFrame to a JSON array
    json_array = commentsColor.toJSON().collect()
    
    resultado = []
    for document in json_array:
        json_object =json.loads(document)
        json_object["color"] = json_object.pop("colorMasRepetido")
        resultado.append(json_object)
    return resultado


def menosDisp():
    commentsDisp = sqlC.sql(
    "SELECT microsNoDisponibles FROM PARADEROS")
    comments_exploded = commentsDisp.select(F.explode("microsNoDisponibles").alias("microsNoDisponibles"))
    comments_exploded.createOrReplaceTempView("PARADEROS_B")
    comments_exploded = sqlC.sql(
    "SELECT microsNoDisponibles, COUNT(microsNoDisponibles) AS cantidad FROM PARADEROS_B GROUP BY microsNoDisponibles ORDER BY cantidad DESC")
    # Convert the DataFrame to a JSON array
    json_array = comments_exploded.toJSON().collect()
  
    resultado = []
    for document in json_array:
        json_object =json.loads(document)
        json_object["micro"] = json_object.pop("microsNoDisponibles")
        resultado.append(json_object)
    return resultado



# Se inicia flask
app = Flask(__name__)
# Ruta para obtener el color mas popular historicamente
@app.route('/color/')
def colorPopular():
    resultado = colorPopularSpark()
    return jsonify(resultado)

# La micro menos disponible
@app.route('/micro/')
def microMenosDisponible():
    resultado = menosDisp()
    return jsonify(resultado)


def buscarParadero(paradero):
    query = f"SELECT * FROM PARADEROS WHERE paradero='{paradero}' ORDER BY 1 DESC LIMIT 1"
    commentsColor = sqlC.sql(query)
    # Convert the DataFrame to a JSON array
    json_array = commentsColor.toJSON().collect()
    resultado = []
    for document in json_array:
        json_object =json.loads(document)
        resultado.append(json_object)
    return resultado

# La micro menos disponible
@app.route('/paradero/<string:paradero>')
def infoParadero(paradero):
    resultado = buscarParadero(paradero)
    return jsonify(resultado[0])

# BLOQUE PRINCIPAL
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
app.run(debug=True)
