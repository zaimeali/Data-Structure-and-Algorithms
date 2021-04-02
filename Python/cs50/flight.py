class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seats(self):
        return self.capacity - len(self.passengers)

    def add_passenger(self, name):
        # print(self.open_seats())
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True


people = [
    "zaime",
    "osama",
    "faraz",
    "anas"
]
flight = Flight(3)

for p in people:
    success = flight.add_passenger(p)
    if success:
        print(f"{p} is added in a flight")
    else:
        print("No available seats")
