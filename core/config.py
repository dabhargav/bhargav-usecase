import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "audit_logs")
DATA_DIR = os.path.join(BASE_DIR, "data", "profiles")

# Ensure the log folder exists
os.makedirs(LOG_DIR, exist_ok=True)
