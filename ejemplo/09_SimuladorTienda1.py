"""
==========================================
SIMULADOR DE TIENDA CON CONTROL DE ACCESO
==========================================

ORDEN DEL EJERCICIO:

Objetivo:
Desarrollar un programa en Python que simule el funcionamiento básico de una tienda por consola.
El programa debe:
- Pedir los datos de un usuario (nombre, edad, ciudad)
- Comprobar si es mayor de edad
- Si puede acceder, permitir realizar una compra (producto, precio, cantidad)
- Calcular el total a pagar
- Mostrar mensajes claros usando f-strings
- Usar funciones, variables, strings, operadores, input(), print() y if

Requisitos técnicos:
1. Todo el programa en un único archivo llamado app_daw.py
2. Contener al menos estas funciones:
   - perfil_usuario()
   - control_acceso(nombre, edad)
   - carrito_compra()
   - main()
3. Conversiones de tipo: int() y float() para edad, precio y cantidad
4. Operadores: >=, *, +
5. Condicionales if/else
6. Solo podrá comprar si tiene 18 años o más

Funcionamiento esperado:
1. Mostrar mensaje de bienvenida
2. Ejecutar perfil_usuario() y mostrar saludo
3. Ejecutar control_acceso()
   - Si edad >= 18: permitir carrito_compra() y mostrar total
   - Si edad < 18: mostrar mensaje de acceso denegado
4. Finalizar programa

Ejemplo de salida:
BIENVENIDO A LA APLICACIÓN DAW

Introduce tu nombre: Ana
Introduce tu edad: 20
Introduce tu ciudad: Madrid

Acceso permitido.

Producto: Teclado
Precio del producto: 25
Cantidad: 2

Total a pagar: 50 euros.
"""

# ==========================================
# APP DAW - SIMULADOR DE TIENDA
# ==========================================

def perfil_usuario():
    print("\n--- PERFIL DE USUARIO ---")

    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    ciudad = input("Introduce tu ciudad: ")

    print(f"\nHola {nombre}, tienes {edad} años y vives en {ciudad}.")

    return nombre, edad


def control_acceso(nombre, edad):
    print("\n--- CONTROL DE ACCESO ---")

    if edad >= 18:
        print(f"{nombre}, acceso permitido.")
        return True
    else:
        print(f"{nombre}, acceso denegado por ser menor de edad.")
        return False


def carrito_compra():
    print("\n--- CARRITO DE COMPRA ---")

    producto = input("Producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad: "))

    total = precio * cantidad

    print(f"\nHas comprado {cantidad} unidades de {producto}.")
    print(f"Total a pagar: {total} euros.")


def main():
    print("BIENVENIDO A LA APLICACIÓN DAW")

    nombre, edad = perfil_usuario()

    acceso = control_acceso(nombre, edad)

    if acceso:
        carrito_compra()
        print("\nGracias por tu compra.")
    else:
        print("\nNo puedes realizar compras.")


# Ejecutar programa
main()
