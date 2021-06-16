"""[Scynced Lights]
Class attributes are "shared"
Instance attributes are not shared.

"""
from os import sync
def sub(x, y):
    return x - y

def sub2(x, y=0):
    return x - y


class Light:

    def __init__(self, sync=None):
        self.on = False
        self

    def is_on(self):
            return self.on

    def toggle(self):
        self.on = not self.on # new - 'not' op
        if self.sync is not None:
            self.sync.on = not self.sync.on


a = Light()
b = Light()
