# Usar una imagen base de Python
FROM alpine:3.18.2

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Se copian los archivos necesarios
COPY  consumidor.py /app

# Instalacion de python y pip
RUN apk add python3 bash py3-pip openjdk11-jdk
RUN pip install pyspark findspark

# Variables
ENV ID=1
ENV NUM_HEBRAS=1
ENV TOPIC="macrohard"
ENV IP_KAFKA="localhost"
ENV PORT_KAFKA="9092"
ENV IP_MONGO="localhost"
ENV PORT_MONGO="27017"

# Comando por defecto al ejecutar el contenedor
CMD [ "python3", "consumidor.py"]