from breezypythongui import EasyFrame
import math

class SquareRootCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Square Root Calculator")

        self.addLabel(text="Enter the Number:", row=0, column=0, sticky="W")
        self.inputField = self.addTextField(text="", row=0, column=1, width=20)

        self.addLabel(text="Square Root:", row=1, column=0, sticky="W")
        self.outputField = self.addTextField(text="", row=1, column=1, width=20, state="readonly")

        self.addButton(text="Calculate", row=2, column=0, columnspan=2, command=self.computeSquareRoot)

    def computeSquareRoot(self):
        try:
            number = float(self.inputField.getText())
            if number < 0:
                raise ValueError("Cannot compute the square root of a negative number.")
            result = math.sqrt(number)
            self.outputField.setText(f"{result:.2f}")
        except ValueError:
            self.messageBox(title="Invalid Input", message="Please enter a valid non-negative number.", width=30)

if __name__ == "__main__":
    SquareRootCalculator().mainloop()
