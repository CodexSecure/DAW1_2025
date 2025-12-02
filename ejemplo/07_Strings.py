# Ejemplos completos de Python Strings

# 1. Crear strings
nombre = "Michele"
mensaje = 'Python es divertido'
print(nombre)       # Michele
print(mensaje)      # Python es divertido

# 2. Acceso a caracteres
texto = "Python"
print(texto[0])     # Primer carácter: P
print(texto[2])     # Tercer carácter: t
print(texto[-1])    # Último carácter: n
print(texto[-2])    # Penúltimo carácter: o

# 3. Slicing (substrings)
print(texto[0:4])   # Del índice 0 al 3: Pyth
print(texto[2:])    # Desde índice 2 hasta el final: thon
print(texto[:3])    # Desde inicio hasta índice 2: Pyt
print(texto[-4:-1]) # Índices negativos: yth
print(texto[0:6:2]) # Cada 2 caracteres: Pto
print(texto[::-1])  # Invertir string: nohtyP

# 4. Longitud del string
print(len(texto))   # 6

# 5. Concatenación y repetición
saludo = "Hola " + nombre
print(saludo)       # Hola Michele
edad = 25
print(f"{nombre} tiene {edad} años.")  # Michele tiene 25 años
print("Ha" * 3)    # HaHaHa

# 6. Métodos de strings
frase = "   Python es divertido  "
print(frase.upper())          # Convertir a mayúsculas: PYTHON ES DIVERTIDO
print(frase.lower())          # Convertir a minúsculas: python es divertido
print(frase.strip())          # Quitar espacios al inicio y al final: Python es divertido
print(frase.lstrip())         # Quitar espacios al inicio: Python es divertido
print(frase.rstrip())         # Quitar espacios al final:    Python es divertido
print(frase.replace("Python","Michele")) # Reemplazar texto: Michele es divertido
print(frase.split())          # Dividir en lista: ['Python', 'es', 'divertido']
print("-".join(frase.split()))# Unir lista con guiones: Python-es-divertido

# 7. Verificación de contenido
texto2 = "Python3"
print(texto2.isalpha())       # Solo letras: False
print(texto2.isdigit())       # Solo números: False
print(texto2.isalnum())       # Letras o números: True
print("abc".isalpha())        # Solo letras: True
print("123".isdigit())        # Solo números: True
print("abc123".isalnum())     # Letras o números: True

# 8. Escapar caracteres especiales
print("Michele dijo: \"Hola!\"")  # Mostrar comillas dentro del string
print("Primera línea\nSegunda línea") # Salto de línea
print("C:\\Users\\Michele")       # Mostrar ruta con barra invertida

# 9. Formateo de strings
print(f"Hola {nombre}, tienes {edad} años")       # f-string
print("Hola {}, tienes {} años".format(nombre, edad))  # Método format
print("Hola %s, tienes %d años" % (nombre, edad))      # Formateo con %

# 10. Ejemplo práctico completo
ciudad = "Barcelona"
frase_completa = f"{nombre} tiene {edad} años y vive en {ciudad}."
print(frase_completa.upper())                     # Convertir a mayúsculas
print(frase_completa.lower())                     # Convertir a minúsculas
print(frase_completa.replace("Barcelona","Madrid"))  # Reemplazar ciudad
print(frase_completa.split())                     # Dividir en lista de palabras
print("-".join(frase_completa.split()))           # Unir palabras con guión
