# Consumidor

El consumidor se encuentra implementado con pyspark, además es creado mediante docker, para ejecutarlo basta con ejecutar el script de runDocker.sh, este script pedirá las variables necesarias para su ejecución. Además se tiene un archivo de prueba para realizar pruebas rápidas.

Es necesario brindar las IPs y puertos de kafka y mongo, ya que al consumir los datos, estos pasan a ser enviados a la base de datos de mongo.