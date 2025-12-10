# Función para pedir una nota por teclado
def pedir_nota(num):
    nota = float(input(f"Introduce la nota {num}: "))
    return nota

# Función para calcular la media aritmética
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

# Función para calcular la nota final ponderada
def calcular_ponderada(n1, n2, n3):
    return n1 * 0.20 + n2 * 0.30 + n3 * 0.50

# Función principal
def main():
    print("=== CÁLCULO DE NOTA FINAL ===")
    x = "Pepe"
    nota1 = pedir_nota(1)
    nota2 = pedir_nota(2)
    nota3 = pedir_nota(3)

    media = calcular_media(nota1, nota2, nota3)
    ponderada = calcular_ponderada(nota1, nota2, nota3)

    print(f"\nLa media aritmética es: {media:.2f}")
    print(f"La nota final ponderada es: {ponderada:.2f}")

# Ejecutar programa
main()