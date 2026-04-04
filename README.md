# IoT Sensor Temperature Dashboard

An interactive data analysis dashboard built with Python and Plotly, analysing real-world IoT temperature sensor data across indoor and outdoor environments.

## Features
- Interactive charts with zoom, hover, and click functionality
- Indoor vs outdoor temperature comparison across 97,000+ sensor readings
- Temperature trend analysis over 5 months (July – December 2018)
- Temperature distribution histogram
- Monthly average temperature breakdown
- Dashboard exported as a standalone HTML file

## Tech Stack
- Python
- pandas (data cleaning and analysis)
- Plotly (interactive visualisations)
- Kaggle dataset: Temperature Readings — IoT Devices

## How to Run
1. Clone the repository
2. Install dependencies: `pip install pandas plotly`
3. Add the dataset file `IOT-temp.csv` to the project folder
4. Run: `python dashboard.py`
5. Dashboard opens in browser automatically, also saved as `temperature_dashboard.html`

## Key Insights
- Outdoor temperatures averaged ~35°C vs indoor ~30°C
- Significant outdoor temperature spike observed in October–November 2018
- Indoor temperatures remained stable (30–32°C) regardless of season
- Outdoor sensors showed much higher variability than indoor sensors

## Author
Shubhi Maurya — github.com/ShubhiMaurya117
