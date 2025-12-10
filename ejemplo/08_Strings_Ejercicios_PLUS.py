# ============================
# EJERCICIO 1 — Procesamiento de texto con input y funciones
# ============================

# Enunciado (texto plano):
# Pide al usuario un texto.
# Crea una función que:
# 1. Limpie los espacios al inicio y final.
# 2. Convierta todo a minúsculas.
# 3. Reemplace "python" por "PYTHON".
# 4. Devuelva el texto final y la longitud antes y después.
# Llama a la función y muestra los resultados.


# Función que procesa un texto
def procesar_texto(texto):
    longitud_original = len(texto)    # medir longitud original

    texto_limpio = texto.strip()      # limpiar espacios
    texto_minus = texto_limpio.lower()  # convertir a minúsculas
    texto_final = texto_minus.replace("python", "PYTHON")  # reemplazar

    longitud_final = len(texto_final)  # medir longitud final

    return texto_final, longitud_original, longitud_final


# Pedir texto al usuario
entrada = input("Ejercicio 1 - Escribe un texto sobre Python: ")

# Llamar a la función
resultado, long_ini, long_fin = procesar_texto(entrada)

# Mostrar resultados
print("\n--- RESULTADOS EJERCICIO 1 ---")
print("Texto procesado:", resultado)
print("Longitud original:", long_ini)
print("Longitud final:", long_fin)



# ============================
# EJERCICIO 2 — Construcción de frase y conteo del producto
# ============================
#
# ORDEN / ENUNCIADO:
# Pide al usuario un nombre, un producto y un precio.
# Luego crea una función que:
#   1. Construya una frase donde el producto aparezca varias veces, por ejemplo:
#         - "Hola NOMBRE, el PRODUCTO cuesta PRECIO euros.
#            El PRODUCTO es uno de los productos más vendidos.
#            Mucha gente compra este PRODUCTO cada mes."
#
#   2. Cree otra frase igual pero con el producto en mayúsculas.
#
#   3. Cuente cuántas veces aparece el producto en la frase original.
#
#   4. Devuelva la frase original, la frase editada y el número de apariciones.
#
# Finalmente, muestra todos los resultados en pantalla.


# Función que crea la frase y cuenta apariciones del producto
def crear_frase(nombre, producto, precio):
    frase_original = (
        f"Hola {nombre}, el {producto} cuesta {precio} euros. "
        f"El {producto} es uno de los productos más vendidos. "
        f"Mucha gente compra este {producto} cada mes."
    )

    producto_mayus = producto.upper()
    frase_editada = (
        f"Hola {nombre}, el {producto_mayus} cuesta {precio} euros. "
        f"El {producto_mayus} es uno de los productos más vendidos. "
        f"Mucha gente compra este {producto_mayus} cada mes."
    )

    apariciones = frase_original.lower().count(producto.lower())

    return frase_original, frase_editada, apariciones


# Solicitar datos al usuario
nombre_input = input("Introduce un nombre: ")
producto_input = input("Introduce un producto: ")
precio_input = input("Introduce un precio: ")

# Convertir precio a número
precio_input = float(precio_input)

# Llamar a la función
f_original, f_editada, veces = crear_frase(nombre_input, producto_input, precio_input)

# Mostrar resultados
print("\n--- RESULTADOS EJERCICIO 2 ---")
print("Frase original:\n", f_original)
print("\nFrase con producto en mayúsculas:\n", f_editada)
print("\nEl producto aparece:", veces, "veces")