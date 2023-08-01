from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import pyspark
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql import functions as F
import json
import os
from dotenv import load_dotenv



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
@app.route('/color/', methods=['GET'])
@cross_origin()
def colorPopular():
    resultado = colorPopularSpark()
    response = jsonify(resultado)
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# La micro menos disponible
@app.route('/micro/', methods=['GET'])
@cross_origin()
def microMenosDisponible():
    resultado = menosDisp()
    response = jsonify(resultado)
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response


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
@app.route('/paradero/<string:paradero>', methods=['GET'])
@cross_origin()
def infoParadero(paradero):
    resultado = buscarParadero(paradero)
    response = jsonify(resultado[0]) 
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def listParaderos():
    query = f"SELECT DISTINCT paradero FROM PARADEROS "
    commentsList = sqlC.sql(query)
    # Convert the DataFrame to a JSON array
    json_array = commentsList.toJSON().collect()
    resultado = []
    for document in json_array:
        json_object =json.loads(document)
        resultado.append(json_object["paradero"])
    return resultado
# Listar paraderos
@app.route('/paraderos/', methods=['GET'])
@cross_origin()
def listaParadores():
    resultado = listParaderos()
    response = jsonify(resultado)
    return response

# BLOQUE PRINCIPAL
#Lectura de variables
load_dotenv()
ip_mongo = os.environ['IP_MONGO']
port_mongo = os.environ['PORT_MONGO']
db_name = os.environ['DB_NAME']
db_collection = os.environ['DB_COLLECTION']


# Configuracion de spark
conf = pyspark.SparkConf().set("spark.jars.packages",
"org.mongodb.spark:mongo-spark-connector_2.12:3.0.1",
    ).setMaster("local").setAppName("SPARK").setAll([
    ("spark.driver.memory", "3g"),
    ("spark.executor.memory", "4g")
    ])

sc = SparkContext(conf = conf)
sqlC = SQLContext(sc)

# Conexión con mongo db
conexion = f"mongodb://{ip_mongo}:{port_mongo}/{db_name}.{db_collection}"
print("######################")
print("Conexion:",conexion)
print("######################")
comments = sqlC.read.format("com.mongodb.spark.sql.DefaultSource").option("spark.mongodb.input.uri",conexion).load()
comments.createOrReplaceTempView(db_collection)


# Se inicio flask
app.run(debug=True)