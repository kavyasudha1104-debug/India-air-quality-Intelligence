import os
try:
    import streamlit as st
    API_KEY = st.secrets["API_KEY"]
except:
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.waqi.info/feed"

CITIES = [
    "delhi", "mumbai", "chennai", "bangalore",
    "hyderabad", "kolkata", "pune", "ahmedabad",
    "jaipur", "lucknow", "chandigarh", "bhopal",
    "patna", "nagpur", "coimbatore"
]