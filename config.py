import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DATA_DIR = os.path.join(BASE_DIR, "data")

AVAILABLE_REPORTS = ["payout"]
POSSIBLE_RATE_KEYS = ["hourly_rate", "rate", "salary"]