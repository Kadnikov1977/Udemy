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
    wheels_number = 6 #переопределяем атрибут
    def __init__(self, name, color, year, isCrashed, massa):    # добавляем в конструктор все атрибуты из класа предка
                                                                # + новый атрибут
        self.massa = massa
        Car.__init__(self, name, color, year, isCrashed) # конструктор должен содержать все атрибуты из класа предка
    def drive(self, city):
        print('Track ' + self.name + ' is driving to ' + city) #переопределяем метод родителя
    def load_cargo(self, weight):
        self.massa += weight
        print('The cargo is loaded. Weight of track is ' + str(self.massa) + ' kg')

new_track = Track('MAN', 'black', 2004, False, 30000)
print(new_track.massa)
new_track.change_color('blue')
print(new_track.color)
print(new_track.wheels_number)
new_track.drive('Moscow')
new_track.load_cargo(2300)