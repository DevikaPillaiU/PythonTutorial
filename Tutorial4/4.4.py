class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def dataprint(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_no}")

student1 = Student("Alice", 101)
student2 = Student("Bob", 102)

student1.dataprint()
student2.dataprint()
