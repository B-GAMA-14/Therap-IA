
from datetime import datetime
user_usage = {}

def check_usage(user_id):
    now = datetime.now()

    if user_id not in user_usage:
        user_usage[user_id] = now
        return True

    elapsed = (now - user_usage[user_id]).seconds / 3000600
    return elapsed <= 20
