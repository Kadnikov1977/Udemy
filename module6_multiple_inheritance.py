class Swimmer:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello {self.name}. I can swim')

class Walker:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello {self.name} I can walk')

class Flyer:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello {self.name} I can fly')

class GameCharacter(Swimmer, Walker, Flyer): # класс GameCharacter наследуется от трех классов
    def __init__(self, name):
        self.name = name
        Swimmer.__init__(self, name)
        Walker.__init__(self, name)
        Flyer.__init__(self, name)

    def greeting(self):
        print(f'Hello. My name is {self.name}')


james = GameCharacter('James')
james.greeting()

print(isinstance(james, Walker)) # проверяем являуеся ли объект james объектом класса Walker
print(isinstance(james, object)) # любые типы данных являются потомками объекта object