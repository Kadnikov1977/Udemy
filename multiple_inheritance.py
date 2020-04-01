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



james = Swimmer('James')
james.greeting()