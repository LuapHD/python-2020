from GeoForm import GeoForm


class Rechteck(GeoForm):

    def __init__(self, a, b):
        GeoForm.__init__(self)
        self.a = a
        self.b = b

    def flaeche (self):
        return self.a * self.b

    def umfang(self):
        return 2 * self.a + 2 * self.b


r = Rechteck(2,3)
print(r.umfang())
print(r.info())
print(r.flaeche())