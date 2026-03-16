import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MAX_DAILY_HOURS = int(os.getenv("MAX_DAILY_HOURS", 3))
