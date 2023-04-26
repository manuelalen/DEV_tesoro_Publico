from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Conexion a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="manolito_lee",
  password="manolito_lee",
  database="tesoro"
)

# Ruta de ejemplo para obtener todos los registros de una tabla
@app.route('/bancocentral')
def obtener_registros():
  # Crea un cursor para ejecutar las consultas
  cursor = db.cursor()
  
  # Ejecuta una consulta en la base de datos
  consulta = "SELECT * FROM bancocentral"
  cursor.execute(consulta)

  # Recupera los resultados de la consulta
  resultados = cursor.fetchall()

  # Crea una lista de diccionarios para los resultados
  registros = []
  for r in resultados:
    registro = {
      'cantidad': r[0],
      'concepto': r[1]
    }
    registros.append(registro)

  # Devuelve los resultados en formato JSON
  return jsonify(registros)

if __name__ == '__main__':
  app.run()
