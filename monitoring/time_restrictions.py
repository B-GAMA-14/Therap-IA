
from datetime import datetime

def is_allowed_time():
    hour = datetime.now().hour
    return 7 <= hour <= 23 or 0 <= hour <= 10
