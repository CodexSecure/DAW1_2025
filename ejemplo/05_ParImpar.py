"""
def par_o_impar(n):
    if n % 2 == 0:
        return "par"
    else:
        return "impar"

while True:
    n = int(input("Introduce el Numero: "))8

    if n == 9:
        print(" Has introducido el numero 9. Fin")
        break
    print(f"El numero: {n} es {par_o_impar(n)}")
"""

def par_o_impar(n):
    if n % 2 == 0:
        print(f"El numero: {n} es Par")
    else:
        print(f"El numero: {n} es Impar")

while True:
    n = int(input("Introduce el Numero: "))

    if n == 9:
        print(" Has introducido el numero 9. Fin")
        break
    par_o_impar(n)
