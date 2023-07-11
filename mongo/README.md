# Cluster de Mongo

En esta carpeta se tienen los docker-compose con los componentes necesarios para la creación del cluster, en cada docker-compose ya se encuentra las configuraciones del contenedor, es decir, el contenedor se inicia de modo replica, shard, etc.

Luego de iniciar los contenedores es necesario ejecutar los scripts para establecer la comunicación entre los contenedores, pueden estar en distintas máquinas. Los scripts poseen el nombre del contenedor donde deberian ser aplicados.

Esta basado en la implementación de https://github.com/minhhungit/mongodb-cluster-docker-compose/tree/master