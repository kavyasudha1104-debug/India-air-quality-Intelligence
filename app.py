import streamlit as st
import pandas as pd
from datetime import datetime
from fetcher import run_fetch
from cleaner import clean_aqi_data
from analyzer import calculate_city_stats, identify_trends
from scorer import calculate_city_health_score
from alerter import generate_alerts
from reporter import generate_excel_report
import io
import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment

st.set_page_config(
    page_title="India Air Quality Intelligence",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 India Air Quality Intelligence System")
st.markdown("Real-time AQI monitoring and health scoring for 15+ Indian cities")

if st.button("🔄 Fetch Live Data Now"):
    with st.spinner("Fetching live AQI data from government API..."):
        raw_df = run_fetch()
        clean_df = clean_aqi_data(raw_df)
        stats_df = calculate_city_stats(clean_df)
        trends = identify_trends(clean_df)
        scored_df = calculate_city_health_score(clean_df)
        alerts = generate_alerts(scored_df, trends)
        st.session_state["scored_df"] = scored_df
        st.session_state["trends"] = trends
        st.session_state["alerts"] = alerts
        st.session_state["fetch_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if "scored_df" in st.session_state:
    scored_df = st.session_state["scored_df"]
    trends = st.session_state["trends"]
    alerts = st.session_state["alerts"]
    fetch_time = st.session_state["fetch_time"]

    st.caption(f"Last updated: {fetch_time}")

    # ── KPI cards ──
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Cities Tracked", len(scored_df))
    col2.metric("Best City", trends["best"].split(",")[0])
    col3.metric("Worst City", trends["worst"].split(",")[0])
    col4.metric("Critical Cities", len(trends["critical"]))

    st.markdown("---")

    # ── Alerts ──
    st.subheader("🚨 Alert System")
    for alert in alerts:
        if "CRITICAL" in alert:
            st.error(f"🔴 {alert}")
        elif "WARNING" in alert:
            st.warning(f"🟠 {alert}")
        else:
            st.success(f"🟢 {alert}")

    st.markdown("---")

    # ── City Filter ──
    st.subheader("🏙️ City Health Score Rankings")

    display_df = scored_df.copy()
    display_df["city_short"] = display_df["city"].apply(lambda x: x.split(",")[0])
    display_df = display_df[["score_rank", "city_short", "aqi", "category", "health_score", "grade"]]
    display_df.columns = ["Rank", "City", "AQI", "Category", "Health Score", "Grade"]

    all_cities = ["All Cities"] + list(display_df["City"].unique())
    selected_city = st.selectbox("Filter by City", all_cities)

    if selected_city != "All Cities":
        filtered_df = display_df[display_df["City"] == selected_city]
    else:
        filtered_df = display_df

    def color_grade(val):
        if val == "A":
            return "background-color: #00B050; color: white"
        elif val == "B":
            return "background-color: #92D050"
        elif val == "C":
            return "background-color: #FFFF00"
        elif val == "D":
            return "background-color: #FF7700; color: white"
        else:
            return "background-color: #FF0000; color: white"

    def color_aqi(val):
        if val <= 50:
            return "background-color: #00B050; color: white"
        elif val <= 100:
            return "background-color: #92D050"
        elif val <= 150:
            return "background-color: #FFFF00"
        elif val <= 200:
            return "background-color: #FF7700; color: white"
        else:
            return "background-color: #FF0000; color: white"

    styled = filtered_df.style\
        .applymap(color_grade, subset=["Grade"])\
        .applymap(color_aqi, subset=["AQI"])

    st.dataframe(styled, use_container_width=True, hide_index=True)

    st.markdown("---")

    # ── Bar Chart ──
    st.subheader("📊 AQI Comparison — All Cities")
    chart_df = display_df[["City", "AQI"]].set_index("City")
    st.bar_chart(chart_df)

    st.markdown("---")

    # ── Download Button ──
    st.subheader("📥 Download Report")

    generate_excel_report(scored_df, trends, alerts)

    with open(f"reports/AQI_Report_{datetime.now().strftime('%Y-%m-%d')}.xlsx", "rb") as f:
        st.download_button(
            label="Download Excel Report",
            data=f,
            file_name=f"AQI_Report_{datetime.now().strftime('%Y-%m-%d')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

else:
    st.info("Click the button above to fetch live AQI data!")