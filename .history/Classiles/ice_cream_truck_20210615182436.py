





class Icecream:

    def __init__(self):
        self.scoops = 0

    def eat(self, scoops):
        if self.scoops < scoops:
            print("Not enough bites left!")
        else:
            self.scoops -= scoops

    def add(self, scoops):
        self.scoops += scoops # new - in-place
