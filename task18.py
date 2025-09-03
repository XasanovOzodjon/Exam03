class Time:
    def __init__(self, hour, min):
        self.hour = hour
        self.min = min
    
    def __lt__(self, other):
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.min < other.min:
            return True
        else:
            return False
    
    
t1 = Time(10, 30)
t2 = Time(12, 15)
print(t1 < t2)