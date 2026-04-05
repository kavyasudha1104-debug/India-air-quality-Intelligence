import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = "b52a7bf22a1f2aa6956366f98b1c0b4e7dc2e0d1"
BASE_URL = "https://api.waqi.info/feed"

CITIES = [
    "delhi", "mumbai", "chennai", "bangalore",
    "hyderabad", "kolkata", "pune", "ahmedabad",
    "jaipur", "lucknow", "chandigarh", "bhopal",
    "patna", "nagpur", "coimbatore"
]