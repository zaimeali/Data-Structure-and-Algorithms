class Car():
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
    
    def price_increase(self):
        self.price = int(self.price) * 1.15
        

# Inheritance
class SuperCar(Car):
    pass

class LuxuryCar(Car):
    def __init__(self, model, year, price, transmission):
        super().__init__(model, year, price)
        self.transmission = transmission

bugatti = SuperCar('Chiron', 2020, 3500000000)
mercedes = LuxuryCar('GLA SUV', 2020, 4240000, 'Auto')

# print(help(bugatti))

print(bugatti.price)
bugatti.price_increase()
print(bugatti.price)

print(mercedes.__dict__)