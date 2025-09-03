class Animal:
    def eat(self):
        print("Animal is eating")
        
    def bark(self):
        print("Animal is barking")

        
class Dog(Animal):
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"Woof! Woof!")
        
    def eat(self):
        print(f"{self.name} is eating dog korn")

d = Dog("Rex")
print(d.name)
d.bark()