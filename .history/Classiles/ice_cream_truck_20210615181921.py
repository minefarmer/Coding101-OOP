class Icecream:

    def __init__(self):
        self.scoops = 0

    def eat(self, scoops):
        if self.scoops < scoops:
            print("Not enough bites left!")
        else: