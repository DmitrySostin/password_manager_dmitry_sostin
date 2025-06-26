import sqlite3
import string
import secrets
from crypto import encription, decription
from generator import generator
from validation import validate_password





# Добавление в базу данных User, Pass
def add_data(user_name, user_pass):
    password, salt = encription(user_pass)
    db = sqlite3.connect('pwr_db.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT, 
                    pass TEXT,
                    salt TEXT
                    )''')
    cursor.execute("INSERT INTO users (name, pass, salt) VALUES (:name, :pass, :salt)", {"name": user_name, "pass": password, "salt": salt})
    db.commit()
    db.close()

# Поиск по базе данных если есть совпвдение то возвращаем картеж
# иначе вавращаем None
def search(user_pass):
    db = sqlite3.connect('pwr_db.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    res = cursor.fetchall()
    #print(res)
    db.commit()
    db.close()
    for data in res:
        #print(data[1])
        if decription(user_pass, data[2], data[3]):# пароль , хешированный пароль, соль
            return data[0]

    #return res


user = "sj4gysn1"
pas = "sj4gysn1"
rang = 'midle'

# проверка надежности пароля
if validate_password(pas): print(f"Пароль ( {pas} ) НЕ надежный!")
else:  print(f"Пароль ( {pas} ) надежный!")

# генератор паролей 4 уровня (litle, midle, top, hard)
# print(generator(10, rang))

# Добавлеине пароля в БД
# add_data(user, pas)


# Поиск по паролю
# test = search(pas)
# print(f'Совпвдение с паролем №{test}')