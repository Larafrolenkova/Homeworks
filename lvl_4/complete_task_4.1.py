# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

try:
    sqlite_connection = sqlite3.connect('teatchers.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
        Student_Id INTEGER PRIMARY KEY,
        Student_Name TEXT NOT NULL,
        School_Id INTEGER NOT NULL,
        FOREIGN KEY (School_id) REFERENCES School(School_id)
        )
        ''')
    
    cursor.execute('''
        Delete from Students
        ''')
    
    sqlite_insert_query = """INSERT INTO Students
                          (Student_Id, Student_name, School_Id)
                          VALUES
                          (201, 'Иван', 1),
                          (202, 'Петр', 2),
                          (203, 'Анастасия', 3),
                          (204, 'Игорь', 4);"""
    count = cursor.execute(sqlite_insert_query)

    sqlite_connection.commit()
    print("Записи успешно вставлены ​​в таблицу Students ", cursor.rowcount)
    
    cursor.execute('''SELECT Student_id, Student_name, School.School_id, School_name FROM Students,School
               where Students.School_Id = School.School_Id and Student_id = ?''',(201,))
    students = cursor.fetchall()

    # Выводим результаты
    for student in students:
      print(student)

        
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")