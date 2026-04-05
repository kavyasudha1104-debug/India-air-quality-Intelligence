def generate_alerts(df, trends):
    """Generate alerts based on AQI data"""
    alerts = []

    # Critical alert
    for city in trends["critical"]:
        city_short = city.split(",")[0]
        alerts.append(f"CRITICAL: {city_short} AQI is above 200 - Hazardous!")

    # Warning alert for grade D and F cities
    bad_cities = df[df["aqi"] > 150]
    for _, row in bad_cities.iterrows():
        city_short = row["city"].split(",")[0]
        alerts.append(f"WARNING: {city_short} AQI is {int(row['aqi'])} - Unhealthy!")

    # Good news alert
    for city in trends["good"]:
        city_short = city.split(",")[0]
        alerts.append(f"GOOD: {city_short} has clean air today - AQI below 50!")

    return alerts

def print_alerts(alerts):
    """Print all alerts"""
    print("\n" + "=" * 40)
    print("ALERT SYSTEM")
    print("=" * 40)
    if alerts:
        for alert in alerts:
            print(f"  {alert}")
    else:
        print("  No critical alerts today!")