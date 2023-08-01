# Usar una imagen base de Python
FROM alpine:3.18.2

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Se copian los archivos necesarios
COPY  main.py /app
COPY .env /app

# Instalacion de python y pip
RUN apk add python3 bash py3-pip openjdk11-jdk
RUN pip install pyspark findspark flask python-dotenv

# Variables
EXPOSE 5000
# Comando por defecto al ejecutar el contenedor
CMD [ "python3", "main.py"]