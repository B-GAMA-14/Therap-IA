
CRISIS_KEYWORDS = ["suicidio", "matarme", "no quiero vivir", "me quiero morir"]

def evaluate_risk(text):
    for word in CRISIS_KEYWORDS:
        if word in text.lower():
            return "critical"
    return "normal"
