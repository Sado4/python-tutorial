# 継承

class Animal:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello, " + self.name)
        

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

dog = Dog(name="Dog")
dog.hello()
# Compare this snippet from modules/my_module.py:
