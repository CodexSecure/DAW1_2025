# ==============================================
# EJERCICIOS AVANZADOS DE BUCLES (INTERACTIVOS)#
# ==============================================

def ejercicio1():
    # EJERCICIO 1: Suma de números pares de una lista
    print("\n=== EJERCICIO 1: Suma de números pares de una lista ===")
    lista = [int(x) for x in input("Introduce números separados por espacios: ").split()]
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    print("La suma de los números pares es:", suma)

def ejercicio2():
    # EJERCICIO 2: Adivinar un número con límite de intentos
    print("\n=== EJERCICIO 2: Adivina el número (1-20) ===")
    import random
    secreto = random.randint(1, 20)  # Número aleatorio entre 1 y 20
    intentos = 0
    max_intentos = 5  # Límite de intentos

    while intentos < max_intentos:
        adivina = int(input(f"Introduce un número entre 1 y 20 (Intento {intentos+1}/{max_intentos}): "))
        intentos += 1
        if adivina < secreto:
            print("Demasiado bajo")
        elif adivina > secreto:
            print("Demasiado alto")
        else:
            print(f"¡Correcto! Número de intentos: {intentos}")
            return  # Sale del ejercicio si acierta

    # Si se agotan los intentos
    print(f"Se han agotado los {max_intentos} intentos. El número secreto era {secreto}.")


def ejercicio3():
    # EJERCICIO 3: Media de números positivos hasta negativo (mejorado)
    print("\n=== EJERCICIO 3: Media de números positivos hasta negativo ===")
    suma = 0
    contador = 0

    while True:
        entrada = input("Introduce un número (negativo para salir): ")
        try:
            num = float(entrada)  # permite decimales
        except ValueError:
            print("Entrada no válida. Debe ser un número.")
            continue

        if num < 0:
            break

        suma += num
        contador += 1

    if contador == 0:
        print("No se introdujeron números positivos.")
    else:
        print(f"\nTotal de números introducidos: {contador}")
        print(f"Suma total: {suma}")
        print(f"Media de los números positivos: {suma / contador:.2f}")


# ==============================================
# MENÚ INTERACTIVO
# ==============================================
while True:
    print("\n--- MENÚ DE EJERCICIOS AVANZADOS ---")
    print("1: Suma de números pares de una lista")
    print("2: Adivinar un número (máx. 5 intentos)")
    print("3: Media de números positivos")
    print("0: Salir")
    opcion = input("Elige un ejercicio (0-3): ")

    if opcion == "1":
        ejercicio1()
    elif opcion == "2":
        ejercicio2()
    elif opcion == "3":
        ejercicio3()
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
