from zxcvbn import zxcvbn


def validate_password(password):
    result = zxcvbn(password)

    if result["score"] < 3:  # Пароль слишком слабый
        #print(result["score"])
        return False
    return True

"""title = "zaq1mko0@AS"
if validate_password(title): print("OK")
else: print("NOT")
"""

