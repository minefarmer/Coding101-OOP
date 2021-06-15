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


    Dot Expression  # To test the method
instance    method name
IceCream     .   eat             ()


    Assigning an attribute is very similar to defining a variable
    self attaches the attribute         attribute       value
    
        self.cubes  =       3

"""
class IceCream:
    def __init__(self):
        print("Created ice cream")

    def eat(self, scoops):
        if self.scoops < scoops:
            print("Not enough bites left!")
        self.scoops -= scoops

    def add(self, scoops):
        self.scoops += scoops

IceCream.eat()  # Traceback (most recent call last):
            # File "/home/rich/Desktop/CarlsHub/Coding101-OOP/Classiles/ice_cream.py", line 37, in <module>
            #     IceCream.eat()
            # TypeError: eat() missing 2 required positional arguments: 'self' and 'scoops'
