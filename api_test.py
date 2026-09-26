import requests
import pandas as pd

# --- Config ---
CITIES = {
    "Delhi": {"latitude": 28.61, "longitude": 77.21},
    "Mumbai": {"latitude": 19.07, "longitude": 72.88},
    "Hyderabad": {"latitude": 17.38, "longitude": 78.49},
}

BASE_URL = "https://api.open-meteo.com/v1/forecast"


def fetch_weather(city_name, latitude, longitude):
    """Fetch hourly temperature data for a given city."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "forecast_days": 1,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.Timeout:
        print(f"[{city_name}] Request timed out.")
        raise
    except requests.exceptions.HTTPError as e:
        print(f"[{city_name}] HTTP error: {e}")
        raise
    except requests.exceptions.RequestException as e:
        print(f"[{city_name}] Request failed: {e}")
        raise

    df = pd.DataFrame({
        "city": city_name,
        "time": data["hourly"]["time"],
        "temperature_2m": data["hourly"]["temperature_2m"],
    })
    df["time"] = pd.to_datetime(df["time"])
    df["temperature_2m"] = df["temperature_2m"].round(1)
    return df


def main():
    all_data = []

    for city_name, coords in CITIES.items():
        print(f"Fetching weather for {city_name}...")
        city_df = fetch_weather(city_name, coords["latitude"], coords["longitude"])
        all_data.append(city_df)

    combined_df = pd.concat(all_data, ignore_index=True)

    print(combined_df.head())
    print(combined_df.info())

    combined_df.to_csv("weather_data.csv", index=False)
    print("Saved to weather_data.csv")


if __name__ == "__main__":
    main()