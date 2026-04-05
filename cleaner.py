import pandas as pd

def get_aqi_category(aqi):
    """Convert AQI number to category label"""
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"


def clean_aqi_data(df):
    """Clean and enrich raw AQI dataframe"""
    print("Cleaning data...")

    # remove rows where AQI is missing
    df = df.dropna(subset=["aqi"])

    # remove duplicate cities
    df = df.drop_duplicates(subset=["city_query"])

    # make sure AQI is a number
    df["aqi"] = pd.to_numeric(df["aqi"], errors="coerce")

    # drop any rows where AQI couldn't be converted
    df = df.dropna(subset=["aqi"])

    # convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # add category column
    df["category"] = df["aqi"].apply(get_aqi_category)

    # sort by AQI worst to best
    df = df.sort_values("aqi", ascending=False).reset_index(drop=True)

    # add rank column
    df["rank"] = df.index + 1

    print(f"Clean data ready: {len(df)} cities")
    return df