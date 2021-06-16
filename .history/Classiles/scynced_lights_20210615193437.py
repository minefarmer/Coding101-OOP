"""[Scynced Lights]
Class attributes are "shared"
Instance attributes are not shared.


"""
def sub(x, y):
    return x - y

def sub2(x, y=0):
    return x - y


class Light:

    

a = Light()
b = Light()
