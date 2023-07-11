# Productor

En esta carpeta se tiene el script "crearProductores.sh" para la creación de contenedores que consumen la api de red, las acciones que realiza son:

1. Dividir los paraderos en distintos archivos, así a cada contenedor creado se le asigna un número de paraderos.
2. Creación de los contenedores, se pide valores como la cantidad de hebras que usara y las direcciones de kafka, además construye la imagen mediante el Dockerfile, contiene los paradores ya segmentados.
3. Puesta en marcha de los contenedores, los contenedores se ejecutan y consumen la API de red para luego ser enviados a kafka.