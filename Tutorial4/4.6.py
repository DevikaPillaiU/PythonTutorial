class Mobile:
    def __init__(self):
        self.company = ""
        self.model = ""
        self.price = 0

    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Company: {self.company}")
        print(f"Model: {self.model}")
        print(f"Price: ₹{self.price}")

# Creating an object and using methods
mob1 = Mobile()
mob1.set_details("Samsung", "Galaxy A54", 28999)
mob1.display_details()
