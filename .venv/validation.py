from zxcvbn import zxcvbn


def validate_password(password):
    result = zxcvbn(password)

    if result["score"] < 3:  # Пароль слишком слабый
        return False
    return True




