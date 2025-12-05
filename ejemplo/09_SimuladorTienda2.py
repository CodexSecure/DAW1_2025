"""
==========================================
SIMULADOR DE TIENDA CON CONTROL DE ACCESO
VERSIÓN EXTREMA CON ERRORES PARA CORREGIR
==========================================

INSTRUCCIONES:
- Este programa contiene errores de varios tipos:
    * Tipos de datos
    * Operadores incorrectos
    * Retornos faltantes
    * Concatenaciones erróneas
    * Nombres de variables inconsistentes
    * Indentación incorrecta
    * Lógica incorrecta en condiciones
- Tu tarea:
    1. Identificar todos los errores.
    2. Corregirlos siguiendo la consigna original.
    3. El programa debe funcionar correctamente según el enunciado.
"""

# ==========================================
# APP DAW - SIMULADOR DE TIENDA
# ==========================================

def perfil_usuario():
 print("--- PERFIL DE USUARIO ---")

 nombre = input("Introduce tu nombre: ")
 edad = input("Introduce tu edad: ")
 ciudad = input("Introduce tu ciudad: ")

 print("Hola " + nombre + " tienes " + edad + " años y vives en " + Ciudad)

def control_acceso(nombre, edad):
 print("\n--- CONTROL DE ACCESO ---")

 if edad = 18:
    print(nombre + " acceso permitido")
    return Verdadero
 else:
  print(nombre + " acceso denegado por ser menor")
  return False

def carrito_compra():
  print("--- CARRITO DE COMPRA ---")

  Producto = input("Producto: ")
  precio = input("Precio del producto: ")
  Cantidad = input("Cantidad: ")

  total = precio * Cantidad
  print("Has comprado " + Cantidad + " unidades de " + producto)
  print("Total a pagar: " + total + " euros")

def main():
    print("BIENVENIDO A LA APLICACIÓN DAW")

    nombre, edad = perfil_usuario()

    acceso = control_acceso(nomre, edad)

    if acceso == True
        carrito_compra()
        print("\nGracias por tu compra.")
    else
        print("\nNo puedes realizar compras.")

main()
