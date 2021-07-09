import math
from GeoForm import GeoForm

class gleichschenkligesDreieck(GeoForm):

    def __init__(self, s):
        GeoForm.__init__(self)
        self.s = s

    def flaeche (self):
        return self.s * self.s / 4 * math.sqrt(3)

    def umfang(self):
        return self.s * 3

gK = gleichschenkligesDreieck(2)
print(gK.umfang())
print(gK.info())
