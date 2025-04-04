from breezypythongui import EasyFrame
import math

class RootCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Square Root Calculator")

      
        self.addLabel(text="Enter Number:", row=0, column=0, sticky="W")
        self.numberField = self.addFloatField(value=0.0, row=0, column=1, width=20)

        self.addLabel(text="Square Root:", row=1, column=0, sticky="W")
        self.resultField = self.addFloatField(value=0.0, row=1, column=1, width=20, precision=2, state="readonly")

        self.addButton(text="Compute", row=2, column=0, columnspan=2, command=self.calculateRoot)

    def calculateRoot(self):
        try:
            number = self.numberField.getNumber()
            if number < 0:
                raise ValueError("Cannot compute square root of a negative number.")
            root = math.sqrt(number)
            self.resultField.setNumber(root)
        except ValueError:
            self.messageBox(title="Invalid Input", message="Please enter a valid non-negative number.")

if __name__ == "__main__":
    RootCalculator().mainloop()
