# -----------------------------------------------
# Trabajo con Variables en Python
# -----------------------------------------------

# Una variable es un "contenedor" que almacena datos.
# Se le asigna un nombre y un valor usando el operador '='.

# Ejemplo básico:
nombre = "Fidel"   # variable de tipo cadena (str)
edad = 35          # variable de tipo entero (int)
altura = 1.75      # variable de tipo flotante (float)
es_estudiante = True  # variable de tipo booleano (bool)

print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?", es_estudiante)
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# Cambiar el valor de una variable
# -----------------------------------------------
edad = 36  # reasignamos un nuevo valor a la variable edad
print(f"Ahora la edad es: {edad}")
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# Operaciones con variables numéricas
# -----------------------------------------------
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b       # siempre devuelve float
division_entera = a // b
resto = a % b
potencia = a ** b

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Resto:", resto)
print("Potencia:", potencia)
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# Concatenación de cadenas (strings)
# -----------------------------------------------
nombre = "Ana"
apellido = "García"

# Usando '+'
nombre_completo = nombre + " " + apellido
print("Nombre completo (concatenación):", nombre_completo)

# Usando f-strings
nombre_completo2 = f"{nombre} {apellido}"
print("Nombre completo (f-string):", nombre_completo2)
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# Variables múltiples en una línea
# -----------------------------------------------
x, y, z = 5, 10, 15
print("x =", x, ", y =", y, ", z =", z)
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# Intercambiar valores de variables
# -----------------------------------------------
a = 1
b = 2
print("Antes del intercambio: a =", a, "b =", b)

# Intercambio sin variable temporal
a, b = b, a
print("Después del intercambio: a =", a, "b =", b)
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# Tipado dinámico en Python
# -----------------------------------------------
# En Python, no es necesario declarar el tipo de la variable.
# Se puede cambiar su tipo en cualquier momento.

var = 100         # inicialmente entero
print("var =", var, "tipo:", type(var))

var = "Hola"      # ahora es cadena
print("var =", var, "tipo:", type(var))

var = 3.14        # ahora es flotante
print("var =", var, "tipo:", type(var))
print("\n" + "-"*50 + "\n")
