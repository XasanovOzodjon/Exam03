class Cart:
    def __init__(self):
        self.products = []
    
    def add_item(self, name, narxi):
        temp_dic = {
            "name" : name,
            "price" : narxi,
            
                    }
        self.products.append(temp_dic)

    def get_total(self):
        summa = 0
        for product in self.products:
            summa += product["price"]
        return summa


cart = Cart()
cart.add_item("Laptop", 2000)
cart.add_item("Mouse", 100)
print(cart.get_total())