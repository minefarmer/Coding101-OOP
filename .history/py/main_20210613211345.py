class IceCream:

    def __init__(self):
        self.scoops = 3

    def eat(self, scoops):
        self.scoops = self.scoops -= scoops

