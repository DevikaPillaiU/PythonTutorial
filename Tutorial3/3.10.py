from breezypythongui import EasyFrame

class BouncingBallSimulator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Bouncing Ball Distance Calculator")

        self.addLabel(text="Initial Height:", row=0, column=0, sticky="W")
        self.heightInput = self.addTextField(text="", row=0, column=1, width=20)

        self.addLabel(text="Bounciness Index:", row=1, column=0, sticky="W")
        self.bounceFactorInput = self.addTextField(text="", row=1, column=1, width=20)

        self.addLabel(text="Number of Bounces:", row=2, column=0, sticky="W")
        self.bounceCountInput = self.addTextField(text="", row=2, column=1, width=20)

        self.addLabel(text="Total Distance:", row=3, column=0, sticky="W")
        self.distanceOutput = self.addTextField(text="", row=3, column=1, width=20, state="readonly")

        self.addButton(text="Calculate Distance", row=4, column=0, columnspan=2, command=self.calculateDistance)

    def calculateDistance(self):
        try:
            initial
