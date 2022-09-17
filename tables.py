# import sqlite3


#--------------------Путь до файла в проекте Task App------------

db_file = "path_sql"

#---------------------------------------------------------------

#Создание таблицы

# try:
#     connectionSQL = sqlite3.connect(db_file)
#     # sqllite_creation_table = '''CREATE TABLE user (
#     #     id INTEGER PRIMARY KEY,
#     #     email TEXT,
#     #     fio TEXT,
#     #     phone TEXT);'''
#     sqllite_creation_task = '''CREATE TABLE tasks (
#         id INTEGER PRIMARY KEY,
#         title TEXT,
#         status TEXT,
#         created_date TEXT,
#         responsible_full_name TEXT);'''
#     cursor = connectionSQL.cursor()
#     print("Подключился")

#     # selectSQL = "select sqllite_version();"
#     cursor.execute(sqllite_creation_task)
#     # cursor.execute(sqllite_creation_table)
#     # record = cursor.fetchall()
#     connectionSQL.commit()
#     print(f"Таблица создана")
#     cursor.close()

# except sqlite3.Error as error:
#     print(f"Ошибка: {error}")

# finally:
#     if connectionSQL:
#         connectionSQL.close()
#         print("Соединение закрыто")