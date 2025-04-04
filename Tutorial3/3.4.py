from breezypythongui import EasyFrame

class TempConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")

        self.addLabel(text="Celsius:", row=0, column=1)
        self.celsiusInput = self.addFloatField(value=0.0, row=1, column=1, width=10)

        self.addLabel(text="Fahrenheit:", row=0, column=0)
        self.fahrenheitInput = self.addFloatField(value=32.0, row=1, column=0, width=10)
        
        
        self.addButton(text=">>>>", row=2, column=0, command=self.convertFtoC)
        self.addButton(text="<<<<", row=2, column=1, command=self.convertCtoF)
    
    def convertFtoC(self):
        fahrenheit = self.fahrenheitInput.getNumber()
        celsius = (fahrenheit - 32) * 5 / 9
        self.celsiusInput.setNumber(celsius)
    
    def convertCtoF(self):
        celsius = self.celsiusInput.getNumber()
        fahrenheit = (celsius * 9 / 5) + 32
        self.fahrenheitInput.setNumber(fahrenheit)
        
if __name__ == "__main__":
    TempConverter().mainloop()
