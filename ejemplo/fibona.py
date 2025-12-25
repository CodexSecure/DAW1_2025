"""def fibonacci(n):
    # Inicializamos los dos primeros números de la secuencia
    a, b = 0, 1

    # Creamos una lista vacía donde guardaremos los números de Fibonacci
    resultado = []

    # Repetimos n veces para obtener los primeros n números de Fibonacci
    for _ in range(n):
        resultado.append(a)  # Añadimos el número actual a la lista
        a, b = b, a + b     # Actualizamos los valores: 'a' toma el valor de 'b', y 'b' la suma de ambos

    return resultado  # Devolvemos la lista con la secuencia generada

print(fibonacci(5))"""
"""
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Imprimir los 50 primeros números
for i in range(7):
    print(fibonacci(i))
"""
"""
def fibonacci(n, nivel=0):
    sangria = "  " * nivel
    print(f"{sangria}Llamada fibonacci({n})")

    if n == 0:
        print(f"{sangria}→ Caso base: fibonacci(0) = 0")
        return 0

    if n == 1:
        print(f"{sangria}→ Caso base: fibonacci(1) = 1")
        return 1

    resultado = fibonacci(n - 1, nivel + 1) + fibonacci(n - 2, nivel + 1)
    print(f"{sangria}← Retorno fibonacci({n}) = {resultado}")
    return resultado

fibonacci(3)
"""
a, b = 0, 1

for i in range(5):
    print(f"Paso {i}")
    print(a)
    a, b = b, a + b
    print(f"A es : {a} y B es: {b}\n")
