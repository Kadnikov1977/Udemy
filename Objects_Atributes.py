# mazda_car = Car(name = 'Mazda', color = 'red', year = 2019, isCrashed= True)
# print(mazda_car.name)
# print(mazda_car.color)
# print(mazda_car.year)
# print(mazda_car.isCrashed)
# print(mazda_car.wheels_number)
#
# bmv_car = Car(name='BMV', color= 'black', year = 2020, isCrashed= 45)
# print(bmv_car.name)
# print(bmv_car.isCrashed)
#
# class Flyers:
#     def __init__(self, name, color, years):
#         self.name = name
#         self.color = color
#         self.years = years
#
# tu_flyers = Flyers(name = 'TU-134', color = 'white', years=2003)
# print(tu_flyers.years)

#
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
# opel_car = Car('Opel', 'grey', 1999, True)
# opel_car.drive(city = 'Uralsk')
# print(opel_car.color)
# opel_car.change_color('yellow')
# print(opel_car.color)

class Circle:
    PI = 3.14
    def __init__(self, radius = 1):
        self.radius = radius
        self.area = Circle.PI * (self.radius ** 2)
        self.lenth = 2 * Circle.PI * self.radius

    # def get_area(self):
    #     return self.PI * (self.radius ** 2)
    #
    # def get_lenth(self):
    #     return 2 * self.PI * self.radius

# circle1 = Circle(3)
# print(circle1.get_area())

circle2 = Circle(5)
# print(circle2.get_area())
# print(circle2.get_lenth())
print(circle2.area)
print(circle2.lenth)