# Ejercicios sobre Strings en Python
# Enunciado y respuesta en el mismo archivo

# EJERCICIO 1
# Enunciado:
# Dado el string nombre = "Michele", muestra por pantalla:
# - La longitud del string
# - El primer caracter
# - El ultimo caracter
# - El string en mayúsculas

nombre = "Michele"
print("Ejercicio 1:")
print("Longitud:", len(nombre))
print("Primer caracter:", nombre[0])
print("Último caracter:", nombre[-1])
print("Mayúsculas:", nombre.upper())
print()

# EJERCICIO 2
# Enunciado:
# Dado el texto = "Python es divertido", muestra:
# - Si contiene la palabra "divertido"
# - Una versión donde se reemplace "divertido" por "fácil"
# - Los primeros 6 caracteres

texto = "Python es divertido"
print("Ejercicio 2:")
print("Contiene 'divertido':", "divertido" in texto)
print("Reemplazo:", texto.replace("divertido", "fácil"))
print("Primeros 6 caracteres:", texto[:6])
print()

# EJERCICIO 3
# Enunciado:
# Crea un string frase = "Hola Michele, bienvenido a Python".
# Muestra:
# - El string completo
# - La palabra "Michele" usando slicing
# - La frase con todo en minúsculas
# - La frase sin espacios al inicio ni al final

frase = "Hola Michele, bienvenido a Python"
print("Ejercicio 3:")
print("Frase completa:", frase)
print("Palabra Michele:", frase[5:12])
print("Minúsculas:", frase.lower())
print("Sin espacios:", frase.strip())

# EJERCICIO 4
# Enunciado:
# Declara dos variables: a = 10 y b = 3.
# Muestra:
# - La suma
# - La resta
# - La multiplicación
# - Un mensaje que diga "El resultado es X" donde X sea la suma.

a = 10
b = 3
print("Ejercicio 4:")
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
resultado = a + b
print("El resultado es", resultado)
print()

# EJERCICIO 5
# Enunciado:
# Crea una variable saludo = "Hola" y otra persona = "Michele".
# Muestra:
# - Los dos strings juntos (concatenación)
# - La longitud del mensaje final
# - La palabra "Hola" repetida 3 veces

saludo = "Hola"
persona = "Michele"
print("Ejercicio 5:")
mensaje = saludo + " " + persona
print("Mensaje completo:", mensaje)
print("Longitud del mensaje:", len(mensaje))
print("Repetición:", saludo * 3)
