from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os

# Преобразуем пароль в ключ
def encription(password, salt = os.urandom(16)):
      # 16 байт (обязательно сохраните её!)
    #print(password)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),  # Алгоритм хеширования
        length=32,  # Длина выходного ключа (32 байта = 256 бит)
        salt=salt,  # Соль
        iterations=100000,  # Количество итераций (чем больше, тем безопаснее)
    )

    pas = password.encode('utf-8')
    #print(pas)
    key = kdf.derive(pas)
    return(key, salt)  # Ключ для хранения в БД

def decription(password, stored_key, saved_salt): # пароль , хешированный пароль, соль
    # При проверке используем ТУ ЖЕ соль и параметры!
    password = password.encode('utf-8')
    #print(password, stored_key, saved_salt)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=saved_salt, iterations=100000)
    try:
        kdf.verify(password, stored_key)  # Не вызывает ошибку = пароль верный
        return True
    except Exception:
        return False


"""pas = "user"
stored_key = b'\xc0.\xef\x04\xd3\x10j\x19Q\x91\\\x14\xed\x93\xff\\|\xd0\xebLK\xf0\xe9\xf8n\xb8v!\x8e/[\xe2'
salt = b'\xd0\xfdH\xdf\xe3\x15\n\xedU\x88>Rq\xe7\xc2\x8d'


t = decription(pas, stored_key, salt)
print(t)"""