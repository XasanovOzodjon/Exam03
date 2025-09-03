class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def to_json(self):
        return {"name": self.name, "price": self.price}
    

p = Product("Laptop", 1500)
print(p.to_json())

