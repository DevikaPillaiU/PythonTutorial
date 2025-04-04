class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(f"The price of {self.model} ({self.year}) is ₹{self.price}")

# Creating two instances
car1 = Car("Toyota Innova", 2020, 1500000)
car2 = Car("Hyundai Creta", 2022, 1800000)

# Calling the cost() method for each instance
car1.cost()
car2.cost()
