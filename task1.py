class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    
    def get_info(self):
        return f"{self.name} {self.model} ({self.year})"
        

car = Car("BMW", "X5", 2020)
print(car.get_info())