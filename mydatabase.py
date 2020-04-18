import sqlite3
conn = sqlite3.connect('mybase_db.db')         # если файла нет, то он создается
c = conn.cursor()
# c.execute('CREATE TABLE myfamely2 (first_name TEXT, last_name TEXT, age INTEGER);')
print("Для вставки данных в базу myfamely2 введите 1")
print("Для вывода всех данных базы myfamely2 введите 2")
select_your_action = input('Введите действие с базой данных ')

if select_your_action == '1':
    first_name = input("Введите имя ")
    second_name = input("Введите фамилию ")
    age = int(input("Введите возраст "))
    # c.execute(f"INSERT INTO myfamely2 VALUES ('{first_name}', '{second_name}', {age});") # Плохой вариант, т. к. возможен SQLInjektion
    insert_query = f"INSERT INTO myfamely2 VALUES (?, ?, ?);"
    c.execute(insert_query, (first_name, second_name, age))
elif select_your_action == '2':
    memb_of_my_fam = c.execute('SELECT * FROM myfamely2;')
    # for row in memb_of_my_fam:
    #     print(row)
    print(memb_of_my_fam.fetchall())

conn.commit()
conn.close()

