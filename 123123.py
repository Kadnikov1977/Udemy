your_number = int(input('ВВедите число от 0 до 100 включительно '))
range_of_num = range(0, 101)
list_of_num = [t for t in range_of_num]
print(your_number)
if your_number not in list_of_num:
    raise ValueError
if type(your_number) is not int:
    raise ValueError