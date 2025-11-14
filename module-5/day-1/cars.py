class Car:
    wheels = 4
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
bmw = Car("BMW", "Red")
audi = Car("Audi", "Blue")

print(f"It is a {bmw.brand}, there are {bmw.wheels} wheels and it is {bmw.color}")
print(f"It is an {audi.brand}, there are {audi.wheels} wheels and it is {audi.color}")