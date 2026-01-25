#Class
class Cat: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
#Object
    def meow(self): 
        return "Meow!"
my_cat = Cat("Alice", 3)
print(my_cat.name)
print(my_cat.age)
print(my_cat.meow())