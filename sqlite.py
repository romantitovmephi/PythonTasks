import sqlite3

DB_NAME = "sqlite_db.db"

# создаем новую базу данных
# with sqlite3.connect(DB_NAME) as sqlite_connect:
#     print(sqlite_connect)
#     print(sqlite3.version)

# создаем новую таблицу
# with sqlite3.connect(DB_NAME) as sqlite_connect:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""
#     sqlite_connect.execute(sql_request)

# добавим записи в таблицу
# courses = [
#     (456, "Data Science course", 156, 45),
#     (789, "Machine Learning course", 345, 78),
#     (894, "SQL course", 45, 12)
# ]
# with sqlite3.connect(DB_NAME) as sqlite_connect:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     # sqlite_connect.execute(sql_request, (123, "Python courses", 145, 24))
#     for course in courses:
#         sqlite_connect.execute(sql_request, course)
#     sqlite_connect.commit()

# запрос данных из таблицы
with sqlite3.connect(DB_NAME) as sqlite_connect:
    sql_request = "SELECT * FROM courses WHERE students_qty>=150"
    sql_cursor = sqlite_connect.execute(sql_request)
    # for record in sql_cursor:
    #     print(record)
    records = sql_cursor.fetchall()
    print(records)
