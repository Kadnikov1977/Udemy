class Car:
    wheels_number = 4 # Предопределенные атрибуты
    def __init__(self, name, color, year, isCrashed): # Иннициализация класса
        self.name = name # Атрибуты класса
        self.color = color # Атрибуты класса
        self.year = year # Атрибуты класса
        self.isCrashed = isCrashed # Атрибуты класса

    def drive(self, city): # Метод класса
        print(self.name +  ' is driving to ' + city)

    def change_color(self, new_color):
        self.color = new_color

class Track(Car): #наследуемся от класса Car
    def __init__(self, name, color, year, isCrashed, massa): # добавляем в конструктор все атрибуты из класа предка
        self.massa = massa
        Car.__init__(self, name, color, year, isCrashed) # конструктор должен содержать все атрибуты из класа предка

new_track = Track('MAN', 'black', 2004, False, 30000)
print(new_track.massa)