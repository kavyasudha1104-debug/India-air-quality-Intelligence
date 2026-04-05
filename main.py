# from fetcher import run_fetch

# print("=" * 40)
# print("INDIA AIR QUALITY TRACKER")
# print("=" * 40)

# df = run_fetch()

# if df is not None:
#     print("\nData Preview:")
#     print(df.to_string(index=False))

# from fetcher import run_fetch
# from cleaner import clean_aqi_data

# print("=" * 40)
# print("INDIA AIR QUALITY TRACKER")
# print("=" * 40)

# raw_df = run_fetch()

# if raw_df is not None:
#     clean_df = clean_aqi_data(raw_df)
#     print("\nCleaned & Ranked Data:")
#     print(clean_df[["rank","city","aqi","category"]].to_string(index=False))

 
from fetcher import run_fetch
from cleaner import clean_aqi_data
from analyzer import calculate_city_stats, identify_trends
from scorer import calculate_city_health_score, print_score_report
from alerter import generate_alerts, print_alerts
from reporter import generate_excel_report

print("=" * 40)
print("INDIA AIR QUALITY TRACKER")
print("=" * 40)

raw_df = run_fetch()

if raw_df is not None:
    clean_df = clean_aqi_data(raw_df)

    print("\nCleaned & Ranked Data:")
    print(clean_df[["rank","city","aqi","category"]].to_string(index=False))

    stats_df = calculate_city_stats(clean_df)
    trends = identify_trends(clean_df)

    scored_df = calculate_city_health_score(clean_df)
    print_score_report(scored_df)

    alerts = generate_alerts(scored_df, trends)
    print_alerts(alerts)

    generate_excel_report(scored_df, trends, alerts)
    print("\nPipeline complete!")