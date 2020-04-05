import random

your_try = 6

my_number = random.randint(0,100)

chiken = 0

while your_try >= 1:
    print(f'У тебя есть {your_try} попыток, чтобы угадать число', end='\n')
    try:
        your_number = int(input('ВВедите целое число от 0 до 100 включительно '))
        range_of_num = range(0, 101)
        list_of_num = [t for t in range_of_num]
        if your_number not in list_of_num:
            raise ValueError
        if type(your_number) is not int:
            raise ValueError
    except ValueError:
        print()
        print('Не корректный ввод, повторите попытку', end='\n\n')
        continue
    if your_number > my_number:
        print('Загаданное число меньше', end='\n\n')
        # print()
    elif your_number < my_number:
        print('Загаданное число больше', end= '\n\n')
        # print()
    else:
        chiken = 1
        break
    your_try = your_try - 1

if chiken == 0:
    print('Ты проиграл лошара!!!')
    print(f'Я загадал число {my_number} ')
else:
    print('Ты угадал - молодец')

input('Для выхода нажми клавишу ENTER')