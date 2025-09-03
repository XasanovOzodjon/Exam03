class Flyer:
    def fly(self):
        print("fly")


class Swimmer:
    def swim(self):
        print("swim")


class Duck(Flyer, Swimmer):
    def fly(self):
        print("Duck is flying")
        
    def swim(self):
        print("Duck is swimming")


duck = Duck()
duck.fly()
duck.swim()