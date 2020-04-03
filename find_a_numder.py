import random

your_try = 6

my_number = random.randint(0,100)

chiken = 0

while your_try >= 1:
    print(f'У тебя есть {your_try} попыток, чтобы угадать число')
    your_number = int(input('ВВедите число от 0 до 100 включительно '))
    print()
    if your_number > my_number:
        print('Загаданное число меньше')
        print()
    elif your_number < my_number:
        print('Загаданное число больше')
        print()
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