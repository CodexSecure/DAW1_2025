import sqlite3

conexion = sqlite3.connect("./ejemplo_bd/cole.db")

cursor = conexion.cursor()

#Consultar datos
print("### Antes de Insertar ###")
cursor.execute("SELECT * FROM users")
filas = cursor.fetchall()

for f in filas:
    print(f)

"""
#Insertar datos a la BD
cursor.execute(
    "INSERT INTO users (nombre_user, edad_user) VALUES (?, ?)",
    ("Pepe", 28)
)
conexion.commit()

print("\n### Despues de Insertar ###")
cursor.execute("SELECT * FROM users")
filas = cursor.fetchall()

for f in filas:
    print(f)

"""

conexion.close()







