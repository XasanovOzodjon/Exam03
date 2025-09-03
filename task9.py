class Temperature:
    def __init__(self, temp):
        self.temp = temp
        
    @property
    def celsius(self):
        return self.temp
    
    @property
    def fahrenheit(self):
        return float(self.temp + 32)
    

t = Temperature(0)
print(t.celsius)
print(t.fahrenheit)