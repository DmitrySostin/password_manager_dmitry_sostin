# Простой (только буквы, длина 6-8 символов)
# Средний (буквы и цифры, длина 8-12 символов)
# Сложный (буквы, цифры, специальные символы, длина 12 16 символов)
# Максимальная сложность (длина 16+ символов, все возможные символы, высокая энтропия)


import string
import secrets

def generator (long, rang):
    if rang == "litle":
        alphabet = string.ascii_letters + string.ascii_lowercase
        password = ''.join(secrets.choice(alphabet) for i in range(long))
    elif rang == "midle":
        alphabet = string.ascii_letters + string.ascii_lowercase + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(long))
    elif rang == "top":
        alphabet = string.ascii_letters + string.ascii_lowercase + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(long))
    elif rang == "hard":
        alphabet = string.printable
        password = ''.join(secrets.choice(alphabet) for i in range(long))
    else: password = "PASS"

    return password

#rang = "hard"
#print(generator(12, rang))