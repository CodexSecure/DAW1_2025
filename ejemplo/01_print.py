# -----------------------------------------------
# Ejemplos básicos de impresión en Python
# -----------------------------------------------

# Imprimir texto simple
print("Hola mundo")
print("\n" + "-"*50 + "\n")

# Imprimir un número entero
print(123)
print("\n" + "-"*50 + "\n")

# Imprimir un valor booleano
print(True)
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# Uso de 'sep' para cambiar el separador entre valores
# -----------------------------------------------
print("2025", "11", "29", sep="-")
print("\n" + "-"*50 + "\n")
# Resultado en pantalla: 2025-11-29


# -----------------------------------------------
# Imprimir varias variables en una sola línea
# -----------------------------------------------
nombre = "Ale"
edad = 30

# print añade espacios entre cada argumento por defecto
print("Nombre:", nombre, "Edad:", edad)
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# f-strings (método moderno y recomendado)
# -----------------------------------------------
print(f"Mi nombre es {nombre} y tengo {edad} años")
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# .format() (método anterior a f-strings)
# -----------------------------------------------
nombre1 = "Ana"
edad1 = "25"

print("Mi nombre es {} y tengo {} años".format(nombre1, edad1))
print("\n" + "-"*50 + "\n")
# Las llaves {} se reemplazan por los valores en orden


# -----------------------------------------------
# Formateo numérico en f-strings
# -----------------------------------------------
pi = 3.141592

# Imprimir con 2 decimales
print(f"{pi:.2f}")   # Resultado: 3.14
print("\n" + "-"*50 + "\n")

# Imprimir con 4 decimales
print(f"{pi:.4f}")   # Resultado: 3.1416
print("\n" + "-"*50 + "\n")
