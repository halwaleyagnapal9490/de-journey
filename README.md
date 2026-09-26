## Project 1: Weather API ETL Pipeline

A simple ETL (Extract, Transform, Load) pipeline that:
- **Extracts** hourly temperature data for multiple cities (Delhi, Mumbai, Hyderabad) from the [Open-Meteo API](https://open-meteo.com/)
- **Transforms** the JSON responses into a clean pandas DataFrame, combining all cities into one dataset with proper datetime parsing and rounded values
- **Loads** the result into a CSV file
- Includes error handling for timeouts, HTTP errors, and network failures
- Uses a config dictionary so new cities can be added with a single line

### Tools used
- Python
- `requests` (API calls)
- `pandas` (data cleaning and transformation)

### How to run
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install requests pandas
python api_test.py
```

### Output
A `weather_data.csv` file with hourly timestamps and temperature readings for each city.

### Next steps
- Load into PostgreSQL instead of CSV
- Schedule with Airflow
- Read city list from an external config file (JSON/YAML)
- Add a Tableau dashboard on top