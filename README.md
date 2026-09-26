# Data Engineering Journey

This repo tracks my hands-on projects as I learn data engineering, starting from the basics.

## Project 1: Weather API ETL Pipeline

A simple ETL (Extract, Transform, Load) script that:
- **Extracts** hourly temperature data from the [Open-Meteo API](https://open-meteo.com/)
- **Transforms** the JSON response into a clean pandas DataFrame (proper datetime parsing, rounded values)
- **Loads** the result into a CSV file

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
A `weather_data.csv` file with hourly timestamps and temperature readings.

### Next steps
- Add error handling and retries
- Load into PostgreSQL instead of CSV
- Schedule with Airflow
- Add a Tableau dashboard on top