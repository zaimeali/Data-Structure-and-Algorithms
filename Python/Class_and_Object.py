class Car():
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
    
    def price_increase(self):
        self.price = int(self.price) * 1.15
        

honda = Car('City', 2021, 5000000)
toyota = Car('Corolla', 2021, 3500000)

# Add New Value
honda.transmission = 'Auto' # only for honda

print(honda.__dict__)
print(toyota.__dict__)

print("Old Price: " + str(honda.price))
honda.price_increase()
print("New Price: " + str(honda.price))
