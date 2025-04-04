from breezypythongui import EasyFrame
import random

class NumberGuessingGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Number Guessing Game")

        self.addLabel(text="Guess a number (1-100):", row=0, column=0, sticky="W")
        self.inputField = self.addIntegerField(value=0, row=0, column=1, width=10)

        self.resultLabel = self.addLabel(text="", row=1, column=0, columnspan=2, sticky="W")

        self.addButton(text="Submit Guess", row=2, column=0, columnspan=2, command=self.checkGuess)
        self.addButton(text="Restart Game", row=3, column=0, columnspan=2, command=self.restartGame)

        self.secretNumber = random.randint(1, 100)
        self.attempts = 0

    def checkGuess(self):
        try:
            userGuess = self.inputField.getNumber()
            if userGuess is None:
                raise ValueError("Invalid input. Please enter a number.")
            
            self.attempts += 1

            if userGuess < self.secretNumber:
                self.resultLabel["text"] = "Too low, try again!"
            elif
