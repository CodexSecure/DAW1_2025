import sqlite3

# Conexión a la base de datos SQLite
conexion = sqlite3.connect("./ejemplo_bd/cole.db")

# Creación del cursor
cursor = conexion.cursor()

# Lista de registros a insertar
# Cada tupla representa una fila de la tabla users
usuarios = [
    ("Ana", 14),
    ("Luis", 15),
    ("Marta", 14),
    ("Carlos", 16)
]

# Sentencia SQL con marcadores de posición (?)
# Esto evita inyecciones SQL y errores de formato
sql = """
INSERT INTO users (nombre_user, edad_user)
VALUES (?, ?)
"""

# Inserción de varios registros de una sola vez
cursor.executemany(sql, usuarios)

# Confirmamos los cambios en la base de datos
conexion.commit()

# Mensaje de confirmación
print("Registros insertados correctamente")

# Cerramos la conexión
conexion.close()
