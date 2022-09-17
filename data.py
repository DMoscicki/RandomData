import sqlite3
from faker import Faker
import random
from random_word import RandomWords
import datetime
from tables import db_file as path

faker = Faker()
word = RandomWords()

###-----------------------------Юзер--------------------------------------

class User:
    
    def __init__(self, fio, email, phone, position = None) -> None:

        self.fio = fio
        self.email = email
        self.phone = phone
        self.position = position

    def user_query(self):

        try:
            connection = sqlite3.connect(path)
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO user (email, fio, phone, position) VALUES ('{self.email}', '{self.fio}', '{self.phone}', '{self.position}');")
            connection.commit()
            cursor.close()

        except sqlite3.Error as err:
            connection.rollback()
            print(f"Ошибка: {err}")
        
        finally:
            if connection:
                connection.close()

#---------------------------------Задача--------------------------------

class Task:

    def __init__(self, title, status, created_date, responsible) -> None:
        self.title = title
        self.status = status
        self.created_date = created_date
        self.responsible = responsible

    def task_query(self):

        try:
            connection = sqlite3.connect(path)
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO tasks (title, status, created_date, responsible_full_name) VALUES ('{self.title}', '{self.status}', '{self.created_date}', '{self.responsible}');")
            connection.commit()
            print("OK")
            cursor.close()

        except sqlite3.Error as err:
            print(f"Ошибка: {err}")

        finally:
            if connection:
                connection.close()

#----------------------------------------Функция запуска обновления---------------------------------------------

def Run_main(listData):

    for _ in range(10):

        fio = faker.name()
        email = faker.email()
        phone = faker.phone_number()
        position = faker.job()
        user = User(fio, email, phone, position)
        user.user_query()

    for _ in range(10):

        random_status = random.choice(listData)
        created = faker.date_between(datetime.date(2022, 1, 1), datetime.date(2022, 8, 30))
        name = faker.name()
        title = word.get_random_word()
        task = Task(title, random_status, created, name)
        task.task_query()

#----------------------------------------------------------------------------------------------------------------