import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "cole.db")

conexion = sqlite3.connect(db_path)

cursor = conexion.cursor()

cursor.execute("SELECT * FROM users")
filas = cursor.fetchall()

for f in filas:
    print(f)

conexion.close()







