# test_env.py
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("AIzaSyAUg_MmrhQcPbjQXUmPsPyeTRU2LmmVQWY")

if api_key:
    print(f"GEMINI_API_KEY found: {api_key[:5]}...") # Print first 5 chars to confirm
else:
    print("GEMINI_API_KEY not found.")