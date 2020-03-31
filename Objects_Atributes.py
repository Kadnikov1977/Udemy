class Car:
    wheels_number = 4
    def __init__(self, name, color, year, isCrashed):
        self.name = name
        self.color = color
        self.year = year
        self.isCrashed = isCrashed

mazda_car = Car(name = 'Mazda', color = 'red', year = 2019, isCrashed= True)
print(mazda_car.name)
print(mazda_car.color)
print(mazda_car.year)
print(mazda_car.isCrashed)
print(mazda_car.wheels_number)

# bmv_car = Car(name='BMV', color= 'black', year = 2020, isCrashed= 45)
# print(bmv_car.name)
# print(bmv_car.isCrashed)

class Flyers:
    def __init__(self, name, color, years):
        self.name = name
        self.color = color
        self.years = years

tu_flyers = Flyers(name = 'TU-134', color = 'white', years=2003)
print(tu_flyers.years)