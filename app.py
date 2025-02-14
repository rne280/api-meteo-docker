import requests
import pandas as pd

# URL de la API y parámetros
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 39.56939,  # Palma de Mallorca
    "longitude": 2.65024,
    "hourly": "temperature_2m"
}

# Hacer la solicitud GET a la API
response = requests.get(url, params=params)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()  # Convertir la respuesta a JSON
    
    # Extraer temperaturas horarias
    temperatures = data["hourly"]["temperature_2m"]
    
    # Calcular la temperatura media
    avg_temp = sum(temperatures) / len(temperatures)
    
    print(f"✅ La temperatura media en Palma de Mallorca es: {avg_temp:.2f}°C")
else:
    print(f"❌ Error en la solicitud: {response.status_code}")
