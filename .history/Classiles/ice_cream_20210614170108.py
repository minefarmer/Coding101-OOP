"""[Practice: Ice Cream]
    Class
keyword     class name
class       Ice:


variable    class
name        name
ice     =   Ice()
"""
class IceCream:
    def __init__(self):
        self.scoops = 3

    def eat(self, scoops):
        if self.scoops < scoops:
            print("Not enough bites left!")
        self.scoops -= scoops

    def add(self, scoops):
        self.scoops += scoops
