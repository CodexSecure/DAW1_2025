# =====================================================
# EJERCICIO 1: Variables y operaciones
# =====================================================

# Declaración de variables
nombre = "Carlos"
edad = 25
altura = 1.78
es_estudiante = True

# Imprimir usando f-string
print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura} m, Estudiante: {es_estudiante}")
print("\n" + "-"*50 + "\n")

# Operaciones con variables numéricas
numero1 = 12
numero2 = 5

print("Suma:", numero1 + numero2)
print("Resta:", numero1 - numero2)
print("Multiplicación:", numero1 * numero2)
print("División:", numero1 / numero2)
print("División entera:", numero1 // numero2)
print("Resto:", numero1 % numero2)
print("Potencia:", numero1 ** numero2)
print("\n" + "-"*50 + "\n")


# =====================================================
# EJERCICIO 2: Asignación múltiple y concatenación
# =====================================================

# Lista de frutas
frutas = ["manzana", "pera", "melocotón"]

# Unpacking
fruta1, fruta2, fruta3 = frutas

# Asignación múltiple con mismo valor
a = b = c = "Python"

# Imprimir concatenando con +
print("Frutas concatenadas:", fruta1 + ", " + fruta2 + ", " + fruta3)
print("Variables con mismo valor concatenadas:", a + ", " + b + ", " + c)

# Imprimir usando f-strings
print(f"Frutas con f-string: {fruta1}, {fruta2}, {fruta3}")
print(f"Variables con mismo valor f-string: {a}, {b}, {c}")
print("\n" + "-"*50 + "\n")


# =====================================================
# EJERCICIO 3: Variables globales y locales
# =====================================================

# Variable global
contador = 0

def aumentar_contador():
    global contador   # usamos la variable global
    contador += 1

# Llamar función 3 veces
aumentar_contador()
aumentar_contador()
aumentar_contador()

print("Contador global después de aumentar:", contador)

# Función con variable local
def contador_local():
    contador = 0  # variable local
    contador += 1
    print("Contador dentro de función local:", contador)

contador_local()

# Comprobar que la variable global no cambió
print("Contador global después de función local:", contador)
print("\n" + "-"*50 + "\n")
