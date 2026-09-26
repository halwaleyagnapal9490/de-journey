import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 28.61,
    "longitude": 77.21,
    "hourly": "temperature_2m",
    "forecast_days": 1,
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()
data = response.json()

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature_2m": data["hourly"]["temperature_2m"],
})

df["time"] = pd.to_datetime(df["time"])
df["temperature_2m"] = df["temperature_2m"].round(1)

print(df.head())
print(df.info())

df.to_csv("weather_data.csv", index=False)
print("Saved to weather_data.csv")