# =====================================================
# TUTORIAL COMPLETO DE VARIABLES EN PYTHON
# =====================================================

# -----------------------------------------------
# 1. Variables básicas y tipos de datos
# -----------------------------------------------

# Cadena de texto (str)
nombre_usuario = "Lucía"
apellido_usuario = "García"

# Números enteros (int)
edad_usuario = 22

# Números decimales (float)
altura_usuario = 1.65

# Booleanos (bool)
tiene_mascota = True

# Imprimir variables
print(f"Nombre: {nombre_usuario} {apellido_usuario}")
print(f"Edad: {edad_usuario} años")
print(f"Altura: {altura_usuario} m")
print(f"Tiene mascota: {tiene_mascota}")
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# 2. Nombres de variables de múltiples palabras
# -----------------------------------------------

# Uso de snake_case (recomendado en Python)
nombre_completo = nombre_usuario + " " + apellido_usuario
edad_actual = edad_usuario
precio_unitario_producto = 12.99

print(f"Nombre completo: {nombre_completo}")
print(f"Edad actual: {edad_actual}")
print(f"Precio unitario: {precio_unitario_producto} €")
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# 3. Asignar múltiples valores
# -----------------------------------------------

# Asignación múltiple con distintos valores
x, y, z = 5, 10, 15
print("Valores asignados:", x, y, z)

# Asignación múltiple con mismo valor
a = b = c = "Python"
print("Múltiples variables con el mismo valor:", a, b, c)

# Unpacking de lista
frutas = ["manzana", "pera", "melocotón"]
primera, segunda, tercera = frutas
print("Frutas unpacking:", primera, segunda, tercera)
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# 4. Variables globales y locales
# -----------------------------------------------

mensaje_global = "¡Bienvenido!"

def saludar():
    # Accede a la variable global
    print("Mensaje desde la función:", mensaje_global)

saludar()
print("Mensaje fuera de la función:", mensaje_global)

# Modificar variable global desde función
contador = 0

def aumentar_contador():
    global contador  # indica que se usará la variable global
    contador += 1

aumentar_contador()
aumentar_contador()
print("Contador global modificado:", contador)
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# 5. Operaciones con variables numéricas
# -----------------------------------------------

numero1 = 12
numero2 = 5

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2           # float
division_entera = numero1 // numero2   # solo parte entera
resto = numero1 % numero2              # residuo
potencia = numero1 ** numero2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Resto:", resto)
print("Potencia:", potencia)
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# 6. Concatenación y f-strings
# -----------------------------------------------

nombre = "Ana"
apellido = "Fernández"

# Concatenación con +
nombre_completo = nombre + " " + apellido
print("Concatenación:", nombre_completo)

# f-strings (recomendado)
print(f"Usando f-string: {nombre} {apellido} tiene {edad_usuario} años")
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# 7. Tipado dinámico y conversiones
# -----------------------------------------------

var = 100          # int
print(var, type(var))

var = "Hola Python" # str
print(var, type(var))

var = 3.1415       # float
print(var, type(var))

# Conversiones (casting)
edad_str = str(edad_usuario)   # int → str
altura_int = int(altura_usuario)  # float → int (pierde decimales)
numero_float = float(numero2)     # int → float

print("Edad como cadena:", edad_str, type(edad_str))
print("Altura como entero:", altura_int, type(altura_int))
print("Número float:", numero_float, type(numero_float))
print("\n" + "-"*50 + "\n")


# -----------------------------------------------
# 8. Buenas y malas prácticas al nombrar variables
# -----------------------------------------------

# Correcto
usuario_activo = True
nombre_completo = "Luis Fernández"
edad_actual = 30

# Incorrecto
# 1nombre = "Ana"   # empieza con número → inválido
# mi-nombre = "Juan" # contiene guion → inválido
# class = "A"        # palabra reservada → inválido

print("Buenas prácticas en nombres de variables mostradas arriba")
print("\n" + "-"*50 + "\n")
