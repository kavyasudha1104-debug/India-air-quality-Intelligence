# India Air Quality Intelligence

An end-to-end air quality monitoring system that turns live AQI data into **city rankings, health scores, alerts, trend insights, and automated reports**.

The project combines data ingestion, cleaning, analysis, scoring, alert generation, and an interactive Streamlit dashboard into a single pipeline.

🔗 **[View Live Dashboard](https://india-air-quality-intelligence-6aeqhy5zvtquu4opwf4gyh.streamlit.app/)**

## What It Does

* Fetches live air quality data from the **World Air Quality Index (WAQI) API**
* Cleans and ranks cities based on AQI
* Calculates city-level statistics and identifies air quality trends
* Converts AQI values into a custom **City Health Score**
* Assigns cities an **A–F health grade**
* Generates automated alerts for unhealthy and critical AQI levels
* Produces a formatted Excel report
* Provides an interactive Streamlit dashboard

## Pipeline

```text
Live AQI API
     ↓
Data Fetching
     ↓
Data Cleaning
     ↓
City Analysis & Trends
     ↓
Health Scoring
     ↓
Alert Generation
     ↓
Excel Report + Streamlit Dashboard
```

## City Health Score

The project converts AQI into a simple **0–100 health score**, where lower AQI results in a higher score.

|     AQI | Health Score | Grade |
| ------: | -----------: | :---: |
|    0–50 |          100 |   A   |
|  51–100 |           80 |   B   |
| 101–150 |           60 |   C   |
| 151–200 |           40 |   D   |
| 201–300 |           20 |   F   |
|    300+ |            0 |   F   |

This provides an easier way to compare cities beyond raw AQI values.

## Alert System

The system automatically generates alerts based on air quality conditions:

* 🔴 **Critical:** AQI above 200
* 🟠 **Warning:** AQI above 150
* 🟢 **Good:** AQI below 50

This turns the project into a simple **monitoring and decision-support system** rather than a static analysis.

## Project Structure

| File               | Purpose                                          |
| ------------------ | ------------------------------------------------ |
| `fetcher.py`       | Fetches AQI data from the external API           |
| `cleaner.py`       | Cleans and prepares AQI data                     |
| `analyzer.py`      | Calculates city statistics and identifies trends |
| `scorer.py`        | Calculates City Health Scores and grades         |
| `alerter.py`       | Generates AQI alerts                             |
| `reporter.py`      | Generates the Excel report                       |
| `main.py`          | Runs the complete data pipeline                  |
| `app.py`           | Runs the interactive Streamlit dashboard         |
| `config.py`        | Stores project configuration                     |
| `requirements.txt` | Python dependencies                              |

## Analytical Workflow

### 1. Data Ingestion

Live AQI information is retrieved through the World Air Quality Index API.

### 2. Data Cleaning

Raw API responses are transformed into a structured dataset suitable for analysis and ranking.

### 3. City-Level Analysis

The system calculates city statistics and identifies notable air quality conditions and trends.

### 4. Health Scoring

AQI values are converted into a standardized health score and A–F grade, making comparisons easier for non-technical users.

### 5. Automated Alerts

Cities crossing unhealthy or critical AQI thresholds are automatically flagged.

### 6. Reporting

Processed results, trends, scores, and alerts are exported into an Excel report for further analysis or sharing.

### 7. Interactive Dashboard

The Streamlit application provides a visual interface for exploring the latest city-level air quality information.

## Tech Stack

**Python · Pandas · NumPy · Streamlit · Requests · openpyxl**

## How to Run

```bash
pip install -r requirements.txt

python main.py

streamlit run app.py
```

`main.py` runs the complete data-processing pipeline, while `app.py` launches the interactive dashboard.

## Data Source

Air quality data is sourced from the **World Air Quality Index (WAQI)**.

The project is designed to work with live API data rather than relying on a static dataset.

## What This Project Demonstrates

* End-to-end data pipeline design
* API-based data ingestion
* Data cleaning and transformation
* Exploratory and operational analytics
* Rule-based scoring systems
* Automated alert generation
* Excel report automation
* Interactive dashboard development
* Turning raw data into actionable information
