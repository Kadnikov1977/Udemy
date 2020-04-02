# print('I will ba a Python developer')

# Выведите на экран результат произведения чисел 3 и 7
#
# Выведите на экран результат возведения числа 4 в степень 3
#
# Выведите на экран результат вычисления остатка от деления числа 29 на 5

# print(3 * 7)
#
# print(4 ** 3)
#
# print(29 % 5)

# Создайте переменные, описывающие автомобиль - модель, цвет, год, количество дверей.
# Поместите в них значения.
# Затем поменяйте цвет автомобиля, присвоив ниже в коде новое значение соответствующей переменной.
# Выведите на экран все значения.  При создании имён переменных используйте подходящие по смыслу слова.
# Воспользуйтесь Google переводчиком, если нужно.
#
# car_model = 'Mitsu'
# car_color = 'white'
# car_year = 2003
# car_num_of_doors = 5
#
# car_year = 2020
#
# print(car_model, car_color, car_year, car_num_of_doors)

# Создайте переменные, в которые будете помещать возраст людей.
# Также создайте переменную, в которой будет храниться количество людей.
# Вычислите и выведите на экран средний возраст человека исходя из данных о возрасте этих пятерых людей.
# Если не знаете формулу вычисления среднего арифметического значения, воспользуйтесь поиском информации в интернете.
# При создании имён переменных используйте подходящие по смыслу слова. Воспользуйтесь Google переводчиком, если нужно.
#
# human1_age = 23
# human2_age = 32
# human3_age = 45
# human4_age = 54
# human_num = 4
# mid_of_age = (human1_age + human2_age + human3_age + human4_age) / human_num
#
# print(mid_of_age)


# Создайте переменные, поместите в них значения - имя, фамилию и возраст.
# Выведите на экран следующее предложение: "Hi! My name is имя фамилия, I'm возраст years old."
# Используйте конкатенацию переменных и строк.
#
# first_name = 'Igor'
# second_name = 'Kadnikov'
# age = 42
#
# print(f'Hi! My name is {first_name} {second_name}, I\'m {age} years old')
#

# Выведите на экран текст детской песенки:
#
# Baa, baa, black sheep,
# Have you any wool?
# Yes sir, yes sir,
# Three bags full
#
# One for the master,
# One for the dame,
# And one for the little boy
# Who lives down the lane
#
# Baa, baa, black sheep,
# Have you any wool?
# Yes sir, yes sir,
# Three bags full
#
# Отступите от левого края расстояние, равное двум табуляциям.
# Выполните перенос текста на новую строку двумя способами

# print('''
# \t\tBaa, baa, black sheep,
# \t\tHave you any wool?
# \t\tYes sir, yes sir,
# \t\tThree bags full
#
# \t\tOne for the master,
# \t\tOne for the dame,
# \t\tAnd one for the little boy
# \t\tWho lives down the lane
# ''')

# Выведите на печать вторую букву l из строки 'Hello Python!'
# Присвойте строку переменной, затем выведите на печать букву
#
charof_l = 'Hello Python!'[3]
print(charof_l)



# Выведите на печать вторую букву l из строки 'Hello Python!'
# Сделайте это без присваивания строки переменной, в одной строке кода.
# Если не знаете, как это сделать, попробуйте погуглить
#
print('Hello Python!'[2])


# Выведите на печать 'He' из строки 'Hello Python!' минимум двумя способами
#
print('Hello Python!'[:2])
print('Hello Python!'[0:2])



# Создайте новую строку 'Path' из строки 'Hello Python!' путём конкатенации части строки и отсутствующего символа.
# Выведите новую строку на печать
r = 'Hello Python!'
charof_he = r[6] + 'a' + r[8:10]
print(charof_he)
