class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, cls2):
        aa = self.a + cls2.a
        bb = self.b + cls2.b
        return Vector(a = aa, b = bb)

    def __str__(self):
        return f"Vector({self.a}, {self.b})"
    
    
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)