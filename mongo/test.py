from pymongo import MongoClient

# Establecer la conexión con MongoDB
client = MongoClient('mongodb://10.0.0.178:2181')

# Obtener la lista de bases de datos
database_names = client.list_database_names()

# Mostrar las bases de datos
for db_name in database_names:
    print(db_name)

