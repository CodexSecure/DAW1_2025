pi = 3.1416

def area_circulo(r):
    return pi * r * r

print("mymodulo.py -> __name__ =", __name__)


if __name__ == "__main__":
    print("solo se ejecuta si mymodulo es ejecutado directamente")
    print(area_circulo(50))
