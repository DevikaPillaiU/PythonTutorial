class Student:
    def __init__(self):
        self.rollno = 0
        self.mark1 = 0
        self.mark2 = 0
        self.total = 0

    def readData(self):
        self.rollno = int(input("Enter roll number: "))
        self.mark1 = int(input("Enter mark1: "))
        self.mark2 = int(input("Enter mark2: "))

    def computeTotal(self):
        self.total = self.mark1 + self.mark2

    def printDetails(self):
        print(f"Roll Number: {self.rollno}")
        print(f"Mark 1: {self.mark1}")
        print(f"Mark 2: {self.mark2}")
        print(f"Total Marks: {self.total}")

# Creating an object and invoking methods
s1 = Student()
s1.readData()
s1.computeTotal()
s1.printDetails()

