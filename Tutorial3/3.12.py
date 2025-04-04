from breezypythongui import EasyFrame

class TextToUpperConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Text to Uppercase Converter")

        self.addLabel(text="Enter Text:", row=0, column=0, sticky="W")
        self.textInput = self.addTextField(text="", row=0, column=1, width=30)

        self.addLabel(text="Result:", row=1, column=0, sticky="W")
        self.resultOutput = self.addLabel(text="", row=1, column=1, columnspan=2, sticky="W")

        self.addButton(text="Convert", row=2, column=0, columnspan=2, command=self.convertToUpper)

    def convertToUpper(self):
        text = self.textInput.getText()
        self.resultOutput["text"] = text.upper()

if __name__ == "__main__":
    TextToUpperConverter().mainloop()
