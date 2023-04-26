import requests

response = requests.get('http://localhost:5000/bancocentral')
data = response.json()

# Aquí puedes hacer lo que necesites con los datos
# Por ejemplo, imprimirlos en la consola
print(data)
