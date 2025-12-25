import json

print("\n" + "-"*40)
json_texto = '{ "nombre": "Ana", "edad": 25 }'
datos = json.loads(json_texto)

print(datos)
print(type(datos))

print("\n" + "-"*40)
json_texto = '{ "activo": true, "nota": null }'
datos = json.loads(json_texto)

print(datos["activo"])  # True
print(datos["nota"])    # None

print("\n" + "-"*40)
persona = {
  "nombre": "Luis",
  "edad": 30,
  "casado": False
}

json_texto = json.dumps(persona)
print(json_texto)
print(type(json_texto))

with open("./JSON/datos.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

print(datos["curso"])

print("\n" + "-"*40)
config = {
  "tema": "oscuro",
  "idioma": "es",
  "autoguardado": True
}

with open("./JSON/config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

print("\n" + "-"*40)
empresa = {
  "nombre": "TechSA",
  "empleados": [
      {"nombre": "Ana", "rol": "Dev"},
      {"nombre": "Luis", "rol": "Admin"}
  ]
}
print(empresa["empleados"][1]["rol"])
