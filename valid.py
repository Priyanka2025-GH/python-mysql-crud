import re

# Username validation
def validate_username(username):
    if len(username) < 5:
        return False, "Username must be at least 5 characters."
    return True, ""

# Password validation
def validate_password(password):

    if len(password) < 8:
        return False, "Password must be at least 8 characters."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit."

    if not re.search(r"[@$!%*?&]", password):
        return False, "Password must contain at least one special character."

    return True, ""