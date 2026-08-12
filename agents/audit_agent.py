import os
import json
from datetime import datetime
from groq import Groq
from core.config import LOG_DIR, DATA_DIR

class AuditAgent:
    def __init__(self):
        # Automatically loads the GROQ_API_KEY from your .env file
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def run_compliance_check(self, request_text):
        # 1. Load customer profile data
        profile_path = os.path.join(DATA_DIR, "customer_profile.json")
        with open(profile_path, "r") as f:
            profile_data = json.load(f)

        # 2. Ask the Groq AI Agent to review the request against the profile
        prompt = f"Review this request: '{request_text}' for this user profile: {json.dumps(profile_data)}. Is it safe to proceed? Answer in 2 short sentences."
        
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # High-quality open-source model on Groq
            messages=[{"role": "user", "content": prompt}]
        )
        decision = response.choices[0].message.content

        # 3. Create an audit log entry
        log_filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        log_path = os.path.join(LOG_DIR, log_filename)
        
        with open(log_path, "w") as log_file:
            log_file.write(f"Timestamp: {datetime.now()}\n")
            log_file.write(f"Request: {request_text}\n")
            log_file.write(f"Decision: {decision}\n")

        return decision, log_filename
