import pandas as pd
import numpy as np

def calculate_aqi_score(aqi):
    """Lower AQI = higher score. Max 100."""
    if aqi <= 50:
        return 100
    elif aqi <= 100:
        return 80
    elif aqi <= 150:
        return 60
    elif aqi <= 200:
        return 40
    elif aqi <= 300:
        return 20
    else:
        return 0

def calculate_city_health_score(df):
    """Calculate overall health score per city"""
    df = df.copy()
    df["health_score"] = df["aqi"].apply(calculate_aqi_score)
    
    df["grade"] = pd.cut(
        df["health_score"],
        bins=[0, 20, 40, 60, 80, 100],
        labels=["F", "D", "C", "B", "A"],
        include_lowest=True
    )
    
    df = df.sort_values("health_score", ascending=False).reset_index(drop=True)
    df["score_rank"] = df.index + 1
    
    return df

def print_score_report(df):
    """Print the health score report"""
    print("\n" + "=" * 40)
    print("CITY HEALTH SCORE REPORT")
    print("=" * 40)
    print(f"{'Rank':<6} {'City':<15} {'AQI':<6} {'Score':<8} {'Grade'}")
    print("-" * 50)
    
    for _, row in df.iterrows():
        city_short = row["city"].split(",")[0]
        print(f"{row['score_rank']:<6} {city_short:<15} {row['aqi']:<6} {row['health_score']:<8} {row['grade']}")