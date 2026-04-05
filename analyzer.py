import pandas as pd

def calculate_city_stats(df):
    """Calculate key stats per city"""
    stats = df.copy()
    stats["aqi_score"] = 100 - (stats["aqi"] / 5)
    stats["aqi_score"] = stats["aqi_score"].clip(0, 100)
    return stats

def identify_trends(df):
    """Identify best and worst cities"""
    best = df[df["aqi"] == df["aqi"].min()]["city"].values[0]
    worst = df[df["aqi"] == df["aqi"].max()]["city"].values[0]
    critical = df[df["aqi"] > 200]["city"].tolist()
    good = df[df["aqi"] <= 50]["city"].tolist()

    print(f"\nBest city today:            {best}")
    print(f"Worst city today:           {worst}")
    print(f"Critical cities (AQI>200):  {critical}")
    print(f"Good air quality cities:    {good}")

    return {
        "best": best,
        "worst": worst,
        "critical": critical,
        "good": good
    }