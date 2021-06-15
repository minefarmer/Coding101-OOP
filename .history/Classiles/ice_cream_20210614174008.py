"""[Practice: Ice Cream]
    Class
keyword     class name
class       Ice:


    Instantiation
variable        class
name            name
("instance")
ice         =   Ice()


    Method  an action or behavior  ==== to add a method, I simply define a function inside the class
         | method name is (eat)
    def eat(self):
        print("hi") # this line is the method content


    To Test the methodDot Expression
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
