class Taschenrechner:

    wert : 0

    def __init__(self):
        self.wert = 0

    def add(self, x):
        self.wert = self.wert + x
        return( self.wert )

    def sub(self, x):
        self.wert = self.wert - x
        return ( self.wert )

    def mult(self, x):
        self.wert = self.wert * x
        return ( self.wert )

    def div(self, x):
        self.wert = self.wert / x
        return (self.wert)

    def mod(self, x):
        self.wert = self.wert % x
        return (self.wert)

    def get_value(self):
        return self.wert

    def reset_value (self):
        self.wert = 0
        return self.wert

    def set_value (self, x):
        self.wert = x
        return self.wert