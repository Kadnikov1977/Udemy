# class Car:
#     wheels_number = 4 # Предопределенные атрибуты
#     def __init__(self, name, color, year, isCrashed): # Иннициализация класса
#         self.name = name # Атрибуты класса
#         self.color = color # Атрибуты класса
#         self.year = year # Атрибуты класса
#         self.isCrashed = isCrashed # Атрибуты класса
#
#     def drive(self, city): # Метод класса
#         print(self.name +  ' is driving to ' + city)
#
#     def change_color(self, new_color):
#         self.color = new_color
#
# class Track(Car): #наследуемся от класса Car
#     wheels_number = 6 #переопределяем атрибут
#     def __init__(self, name, color, year, isCrashed, massa):    # добавляем в конструктор все атрибуты из класа предка
#                                                                 # + новый атрибут
#         self.massa = massa
#         Car.__init__(self, name, color, year, isCrashed) # конструктор должен содержать все атрибуты из класа предка
#     def drive(self, city):
#         print('Track ' + self.name + ' is driving to ' + city) #переопределяем метод родителя
#     def load_cargo(self, weight):
#         self.massa += weight
#         print('The cargo is loaded. Weight of track is ' + str(self.massa) + ' kg')
#
# new_track = Track('MAN', 'black', 2004, False, 30000)
# print(new_track.massa)
# new_track.change_color('blue')
# print(new_track.color)
# print(new_track.wheels_number)
# new_track.drive('Moscow')
# new_track.load_cargo(2300)

# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying woof')
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying meow')
#
# class Mouse:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying pee-pee-pee')
#
# spike = Dog('Spike')
# tom = Cat('Tom')
# jerry = Mouse('Jerry')
#
# pet_list = [spike, tom, jerry]
#
# def pet_voice(pet):
#     pet.speak()
#
# for pet in pet_list:
#     pet_voice(pet)

# =================================================================================================

# Задания

# Создайте класс GameCharacter с атрибутами name, health, level и методом speak(),
# который выводит на печать 'Hi, my name is (значение атрибута name)'.

# Создайте класс Villain, наследник класса GameCharacter с теми же атрибутами,
# методом speak(), который выводит на печать 'Hi, my name is (значение атрибута name) and I will kill you',
# методом kill(), который принимает в качестве параметра объект класса GameCharacter,
# присваивает атрибуту health этого объекта значение 0 и  выводит на печать 'Bang-bang, now you're dead'

class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print(f'Hi, my name is {self.name} ')

harrychpoker = GameCharacter('Harrychpoker', 30000, 80)
harrychpoker.speak()

class Villain(GameCharacter):
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print(f'Hi, my name is {self.name} and I will kill you')

    def kill(self, other):
        other.health = 0
        print(f'Bang-bang, now {other.name} you\'re dead')

lich = Villain('Lich', 100000, 90)
lich.speak()
lich.kill(harrychpoker)
print(harrychpoker.health)