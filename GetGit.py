import mysql.connector
import json
import git
import shutil

# Conectamos con la base de datos
conexion = mysql.connector.connect(
  host="localhost",
  user="manolito_lee",
  password="manolito_lee",
  database="tesoro"
)

# Creamos un cursor para realizar la consulta
cursor = conexion.cursor()

# Realizamos la consulta
consulta = "SELECT * FROM bancocentral"
cursor.execute(consulta)

# Obtenemos los datos y los guardamos en una lista de diccionarios
registros = []
for registro in cursor:
    registro_dict = {
        "cantidad": registro[0],
        "concepto": registro[1]
    }
    registros.append(registro_dict)

# Cerramos la conexión con la base de datos
conexion.close()

# Creamos un archivo JSON con los datos obtenidos
with open("datos.json", "w") as archivo_json:
    json.dump(registros, archivo_json)
