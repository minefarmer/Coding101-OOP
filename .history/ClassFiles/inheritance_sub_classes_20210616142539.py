"""[Practice: Deluxe Ice Cream Truck]

        child class     parent class
class   Ice             (H2O):
    pass
    | expression



"""



from sympy import real_root


class Icecream:

    max_scoops = 3

    def __init__(self):
        self.scoops = 0

    def eat(self, scoops):
        if self.scoops < scoops:
            print("Not enough bites left!")
        else:
            self.scoops -= scoops

    def add(self, scoops):
        self.scoops += scoops # new - in-place op
        if self.scoops > self.max_scoops:
            self.scoops = 0
            print("Too many scoops! Dropped ice cream.")

class IceCreamTruck:
    def order(self, scoops):
        self.sold = 0

    def order(self, scoops):
        ice_cream = Icecream()
        self.add(ice_cream, scoops)
        return ice_cream

    def add(self, ice_cream, scoops):
        ice_cream.add(scoops)
        self.sold += scoops




class DeluxeIceCreamTruck(IceCreamTruck):
    pass

