import sqlite3
import string
import secrets
import pyperclip
from typing import Optional
from crypto import encription, decription
from generator import generator
from validation import validate_password
from db_crate import add_data, search
from copy import write
from export import export_to_csv, export_to_json, export_to_sql

#user = "sj4gysn1"
#pas = "sj4gysn1"
#rang = 'midle'

# проверка надежности пароля
#if validate_password(pas): print(f"Пароль ( {pas} ) НЕ надежный!")
#else:  print(f"Пароль ( {pas} ) надежный!")

# генератор паролей 4 уровня (litle, midle, top, hard)
# print(generator(10, rang))

# Добавлеине пароля в БД
# add_data(pas)


# Поиск по паролю
#test = search(pas)
#print(f'Совпвдение с паролем №{test}')

def get_complexity() -> Optional[str]:
    rang = input(">>> (L)itle, (M)midle, (T)op, (H)ard pass:\n<<< ").lower()
    if rang == "l":
        return "litle"
    elif rang == "m":
        return "midle"
    elif rang == "t":
        return "top"
    elif rang == "h":
        return "hard"
    else:
        print(">>> Incorrect choice of difficulty! Try again.")
        return None

def get_length() -> int:
    while True:
        try:
            length = int(input(">>> Enter the desired number of characters (min 6 symbols):\n<<< "))
            return max(6, length)
        except ValueError:
            print(">>> Pleace enter number!")

def collection_generator():
    complexity = None
    while complexity is None:
        complexity = get_complexity()

    length = get_length()
    password = generator(length, complexity)
    print(f">>> Your pass >>>-{password}-<<<")
    copyrite = input(">>> Copy this password (Y)es/(N)o ?\n<<< ").lower()
    if copyrite == "y": write(password)
    print(f">>> Password >-{password}-< copied to clipboard.")

def collection_add():
    rang = input(">>> Adding password to DB.\n>>> Enter your password\n<<< ")
    if add_data(rang): print(">>> Data added to DB")

def collection_search():
    rang = input(">>> Search password by DB.\n>>> Enter search password\n<<< ")
    if search(rang): print(f">>> >-{rang}-<\n>>> Such data is in DB")
    else: print(f">>> >-{rang}-<\n>>> Such data is NOT in DB")

def collection_export():
    rang = None
    print(">>> Export DB in:")
    print(">>> (1) Export to CSV (encripted)")
    print(">>> (2) Export to JSON (encripted)")
    print(">>> (3) Export to SQL dump")
    rang = input("<<< ")
    if rang.isdigit():
        if int(rang) == 1: export_to_csv("pwr_db.db")
        elif int(rang) == 2: export_to_json("pwr_db.db")
        elif int(rang) == 3: export_to_sql("pwr_db.db")
        else:
            print(">>> Key 1 to 3\n>>> Try again!")
            collection_export()
    else:
        print(">>> Incorrect input!\n>>> Try again!")
        collection_export()

def select_function():
    key = input(">>> (Q)uit, (G)enerate pass, (S)earch pass, (A)dd pass, (V)alidate, (E)xport:\n<<< ").lower()
    if key == "q":
        print(f">>> User complited the programm!!!")
        exit()
    elif key == "g":# вызываем сбор для генератора паролей
        collection_generator()
    elif key == "s":# Вызываем сбор для поиску по БД
        collection_search()
    elif key == "a":# Вызываем сбор для добавления в БД
        collection_add()
    elif key == "v":# Вызываем сбор для проверки пароля на вшивость
        pas = input(">>> Enter password to verify!\n<<< ")
        if validate_password(pas): print(f"Password >-{pas}-< is strong!")
        else: print(f"Password >-{pas}-< is not secure!")
    elif key == "e":# Вызываем сбор для экспорта БД
        collection_export()
    else:
        print(f">>> Unnoung command, try again")

while True:
    select_function()


"""
while True:
    key = input(">>> (Q)uit, (G)enerate pass, (S)earch pass, (A)dd pass, (V)alidate:\n<<< ")

    if key.lower() == "q":
        exit()
    elif key.lower() == "g":
        rang = input(">>> (L)itle, (M)midle, (T)op, (H)ard pass:\n<<< ")
        simmbols = int(input(">>> Enter the desired number of characters (min 6 simbols):\n<<< "))
        if rang.lower() == "l":  rang = "litle"
        elif rang.lower() == "m": rang = "midle"
        elif rang.lower() == "t": rang = "top"
        elif rang.lower() == "h": rang = "hard"
        else:
            key = "g"

        if simmbols < 6: simmbols = 6
        print(f">>> Your pass >>>{generator(simmbols, rang)}<<<")
"""