# India-air-quality-Intelligenc
# India Air Quality Intelligence System

Real-time AQI monitoring and intelligence system for 15+ Indian cities.

## What it does
- Fetches live AQI data from WAQI Government API
- Cleans and ranks cities by air quality
- Custom City Health Score algorithm (A-F grading)
- Automated alert system for critical AQI spikes
- Colour-coded Excel report auto-generation
- Interactive Streamlit dashboard

## Tech Stack
Python, Pandas, NumPy, Streamlit, openpyxl, requests

## Pipeline Structure
API → Data Cleaning → Analysis → Scoring → Alerts → Excel Report

## City Health Score Formula
- AQI 0-50 → Grade A (Excellent)
- AQI 51-100 → Grade B (Good)
- AQI 101-150 → Grade C (Moderate)
- AQI 151-200 → Grade D (Poor)
- AQI 200+ → Grade F (Critical)

## How to Run
pip install -r requirements.txt
python main.py
streamlit run app.py

## Data Source
World Air Quality Index (WAQI) - aqicn.org
