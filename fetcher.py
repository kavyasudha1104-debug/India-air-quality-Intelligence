import requests
import pandas as pd
from datetime import datetime
from config import API_KEY, BASE_URL, CITIES
import time
import os

def fetch_city_aqi(city_name):
    """Fetch AQI data for one city from the API"""
    try:
        url = f"{BASE_URL}/{city_name}/?token={API_KEY}"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data["status"] == "ok":
            aqi_value = data["data"]["aqi"]
            city_display = data["data"]["city"]["name"]
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

            return {
                "city": city_display,
                "city_query": city_name,
                "aqi": aqi_value,
                "timestamp": timestamp
            }
        else:
            print(f"Could not fetch data for {city_name}")
            return None

    except Exception as e:
        print(f"Error fetching {city_name}: {e}")
        return None


def fetch_all_cities():
    """Fetch AQI for all cities and return as DataFrame"""
    print("Fetching AQI data for all cities...")
    results = []

    for city in CITIES:
        print(f"  Fetching: {city}")
        result = fetch_city_aqi(city)
        if result:
            results.append(result)
        time.sleep(1)  # be polite to the API

    df = pd.DataFrame(results)
    print(f"\nSuccessfully fetched data for {len(df)} cities")
    return df


def save_raw_data(df):
    """Save fetched data to CSV"""
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"data/raw_aqi_{date_str}.csv"
    df.to_csv(filename, index=False)
    print(f"Raw data saved to {filename}")
    return filename


def run_fetch():
    """Main function — fetch and save"""
    df = fetch_all_cities()
    if not df.empty:
        save_raw_data(df)
        return df
    else:
        print("No data fetched. Check your API key.")
        return Nonep