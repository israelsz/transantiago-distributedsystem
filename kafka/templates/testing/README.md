
# Testing

En esta carpeta se encuentra una forma de hacer cluster con imagenes distintas al cluster que fue probado, esta imagen de confluentinc tienen más documentación y soporte por lo que sería beneficioso hacer un cluster con estas imagenes.

## Comandos para esta imagen especifica de kafka [Confluentinc]
### Crear Topic
* Para crear un topic entrar en cualquier instancia de kafka dentro de cualquier docker perteneciente al cluster 
```bash
  docker exec -it <nombre-contenedor-kafka> /bin/bash
```
* Crear un topic (la tubería): Reemplazar <direccion> por la ip de cualquier maquina que este ejecutando una instancia de kafka
* El factor de replicación se recomienda sea 2, no puede ser mayor a la cantidad de brokers (instancia de kafka) existentes en el cluster, sino tira error.
* Para el numero de particiones:
  * Si se tienen menos de 6 brokers en el cluster: el numero de particiones debe ser 3*Cantidad de brokers en el cluster.
  * Para más de 12 brokers usar: 2*Cantidad de brokers en el cluster.
  * Fuente: https://www.conduktor.io/kafka/kafka-topics-choosing-the-replication-factor-and-partitions-count/

```bash
  kafka-topics --bootstrap-server <direccion>:9092 --create --topic randomTopic --replication-factor 3 --partitions 6
```
### Producir mensajes desde la terminal

* Entrar en un contenedor que tenga kafka perteneciente al cluster
```bash
  docker exec -it <nombre-contenedor-kafka> /bin/bash
```
* Reemplazar <direccion> por la ip de cualquier maquina que este ejecutando una instancia de kafka
```bash
  kafka-console-producer --bootstrap-server <direccion>:9092 --topic randomTopic
```

### Leer mensajes desde la terminal (consumir)

* Entrar en un contenedor que tenga kafka perteneciente al cluster
```bash
  docker exec -it <nombre-contenedor-kafka> /bin/bash
```
* Reemplazar <direccion> por la ip de cualquier maquina que este ejecutando una instancia de kafka
```bash
  kafka-console-consumer --bootstrap-server <direccion>:9092 --topic randomTopic --from-beginning
```
