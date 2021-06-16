"""[Scynced Lights]
Class attributes are "shared"
Instance attributes are not shared.


"""
def sub(x, y):
    return x - y

def sub2(x, y=0):
    return x - y


class Light:

    def __init__(self, sync=None):
        self.on = False
        self.sync = sync

    def is_on(self):
            return self.on

    def toggle(self):
        self.on = not self.on # new - 'not' op


a = Light()
b = Light()
