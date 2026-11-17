# strength_checker.py
import math

def entropie(password):
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(not c.isalnum() for c in password):
        charset_size += 32  # symboles

    entropy = len(password) * math.log2(charset_size) if charset_size else 0
    return round(entropy, 2)

def evaluer_force(entropy):
    if entropy < 40:
        return "🟥 Faible"
    elif entropy < 60:
        return "🟧 Moyenne"
    elif entropy < 80:
        return "🟨 Forte"
    else:
        return "🟩 Très forte"
