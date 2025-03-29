class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0 # default speed
    
    def accelerate(self):
        self.speed += 10
        print("The car is accelerating")
    
    def brake(self):
        self.speed -= 10
        print("The car is braking")
        
my_car = car("Toyota", "Corolla", 2015)
print(my_car.brand)
print(my_car.model)
print(my_car.year)
my_car.accelerate()
my_car.brake()