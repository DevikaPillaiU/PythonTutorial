class Arith:
    def read(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"

# Example usage
obj = Arith()
obj.read()
print("Sum:", obj.add())
print("Difference:", obj.subtract())
print("Product:", obj.multiply())
print("Quotient:", obj.divide())
