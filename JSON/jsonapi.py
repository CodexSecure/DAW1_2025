import requests

# Hacemos una solicitud GET a la API
respuesta = requests.get("https://jsonplaceholder.typicode.com/users/1")

# Convertimos la respuesta JSON a un diccionario de Python
datos = respuesta.json()

# Ahora podemos acceder a los campos como en un diccionario
print("ID:", datos["id"])
print("Nombre:", datos["name"])
print("Correo:", datos["email"])
