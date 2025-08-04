import requests

print("🔮 API Agify - Predicción de edad por nombre")
nombre = input("👉 Ingresá un nombre: ")
pais = input("🌎 Ingresá el código del país (ej: AR, ES, MX): ")

url = "https://api.agify.io"
params = {"name": nombre, "country_id": pais}

respuesta = requests.get(url, params=params)

if respuesta.status_code == 200:
    datos = respuesta.json()
    print("\n📊 Resultado:")
    print(f"Nombre: {datos['name']}")
    print(f"Edad estimada: {datos['age']} años")
    print(f"Personas analizadas: {datos['count']}")
else:
    print("❌ Error al consultar la API")
