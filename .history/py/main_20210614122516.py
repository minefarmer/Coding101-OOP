class Light:
    def __init__(self):
        self.on = False

    def toggle(self):
        if self.on:
            self.on = False
        else:
            self.on = True
        

