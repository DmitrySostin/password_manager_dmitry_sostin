import sqlite3
from crypto import encription, decription

# Добавление в базу данных User, Pass
def add_data(user_pass):
    password, salt = encription(user_pass)
    db = sqlite3.connect('pwr_db.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT, 
                    pass TEXT,
                    salt TEXT
                    )''')
    cursor.execute("INSERT INTO users (name, pass, salt) VALUES (:name, :pass, :salt)", {"name": user_pass, "pass": password, "salt": salt})
    db.commit()
    db.close()
    return True

# Поиск по базе данных если есть совпвдение то возвращаем картеж
# иначе вавращаем None
def search(user_pass):
    db = sqlite3.connect('pwr_db.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM ")
    res = cursor.fetchall()
    #print(res)
    db.commit()
    db.close()
    for data in res:
        #print(data[1])
        if decription(user_pass, data[2], data[3]):# пароль , хешированный пароль, соль
            return data[0]

    #return res
    
# Добавлеине пароля в БД
# add_data(user, pas)


# Поиск по паролю
#pas = ("zaq1mko0@AS")

#test = search(pas)
#print(f'Совпвдение с паролем №{test}')