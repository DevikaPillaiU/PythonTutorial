from breezypythongui import EasyFrame
import math

class SquareRootFinder(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Square Root Finder")

        self.addLabel(text="Enter a Number:", row=0, column=0, sticky="W")
        self.inputField = self.addFloatField(value=0.0, row=0, column=1, width=20)

        self.addLabel(text="Square Root:", row=1, column=0, sticky="W")
        self.outputField = self.addFloatField(value=0.0, row=1, column=1, width=20, precision=2, state="readonly")

        self.addButton(text="Calculate", row=2, column=0, columnspan=2, command=self.calculateSquareRoot)

    def calculateSquareRoot(self):
        try:
            number = self.inputField.getNumber()
            if number < 0:
                raise ValueError("Cannot compute the square root of a negative number.")
            result = math.sqrt(number)
            self.outputField.setNumber(result)
        except ValueError:
            self.messageBox(title="Invalid Input", message="Please enter a valid non-negative number.")

if __name__ == "__main__":
    SquareRootFinder().mainloop()
