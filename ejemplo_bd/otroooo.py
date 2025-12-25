import sqlite3

conexion = sqlite3.connect("./ejemplo_bd/cole.db")
cursor = conexion.cursor()

cursor.executemany(
    "INSERT INTO users (nombre_user, edad_user) VALUES (?, ?)",
    [
        ("Pepe", 28),
        ("Ana", 22),
        ("Luis", 31),
        ("Marta", 25)
    ]
)

conexion.commit()
conexion.close()
