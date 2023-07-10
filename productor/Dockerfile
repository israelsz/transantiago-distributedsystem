# Usar una imagen base de Python
FROM alpine:3.18.2

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Se copian los archivos necesarios
COPY  productor.py /app
COPY  partes /app

# Instalacion de python y pip
RUN apk add python3
RUN apk add py3-pip

# Instalar las dependencias del proyecto
RUN pip install requests
RUN pip install kafka-python==2.0.2

# Variables
ENV ID=1
ENV NUM_HEBRAS=1
ENV TOPIC="macrohard"
ENV IP_KAFKA="localhost"
ENV PORT_KAFKA="9092"

# Comando por defecto al ejecutar el contenedor
CMD [ "python3", "productor.py"]