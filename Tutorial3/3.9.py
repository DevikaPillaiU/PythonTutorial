from breezypythongui import EasyFrame
import random

class NumberGuesser(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Number Guessing Assistant")

        self.addLabel(text="Think of a number (1-100).", row=0, column=0, columnspan=2, sticky="NSEW")
        self.guessLabel = self.addLabel(text="", row=1, column=0, columnspan=2)

        self.smallerButton = self.addButton(text="Too Small", row=2, column=0, command=self.guessHigher)
        self.largerButton = self.addButton(text="Too Large", row=2, column=1, command=self.guessLower)
        self.correctButton = self.addButton(text="Correct!", row=3, column=0, columnspan=2, command=self.guessCorrect)
        self.newGameButton = self.addButton(text="New Game", row=4, column=0, columnspan=2, command=self.startNewGame)

        self.lowerLimit, self.upperLimit, self.attempts = 1, 100, 0
        self.makeGuess()

    def makeGuess(self):
        if self.lowerLimit <= self.upperLimit:
            self.currentGuess = (self.lowerLimit + self.upperLimit) // 2
            self.guessLabel["text"] = f"Is it {self.currentGuess}?"
        else:
            self.guessLabel["text"] = "Please start a new game."

    def guessHigher(self):
        self.lowerLimit = self.currentGuess + 1
        self.attempts += 1
        self
