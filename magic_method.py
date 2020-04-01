class Person:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def __str__(self): # переопределяем встроенный метод print
        return self.first_name + ' ' + self.second_name

    def __len__(self): # переопределяем встроенный метод len
        return len(self.first_name) + len(self.second_name)

jack = Person('Igor', 'Kadnikov', 42)

print(jack)
print(len(jack))