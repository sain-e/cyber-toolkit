from zxcvbn import zxcvbn
import bcrypt

def check_strength(password):
    result = zxcvbn(password)
    score = result["score"]
    if score == 3:
        response = f"Strong enough password: Score of {score}" # 3
    elif score == 4:
        response = f"Very strong password: Score of {score}" # 4
    else:
        feedback = result.get("feedback")
        warning = feedback.get("warning")
        suggestions = feedback.get("suggestions")
        response = f"Weak password: Score of {score}" # 0, 1, 2
        response += f"\nWarning: {warning}"
        response += "\nSuggestions: "
        for suggestion in suggestions:
            response += suggestion
    return response

def hash_password(password):
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(password.encode(), salt)
    return password_hashed

def verify_password(password_attempt, password_hashed):
    if bcrypt.checkpw(password_attempt.encode(), password_hashed):
        return "Password is correct. Access granted!"
    else:
        return "Incorrect password. Access denied."
