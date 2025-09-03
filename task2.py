class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, studying in {self.course}nd course."
        

s = Student("Ali", 20, 2)
print(s.introduce())