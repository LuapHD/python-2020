from GeoForm import GeoForm


class Quadrat(GeoForm):

    def __init__(self, a):
        GeoForm.__init__(self)
        self.a = a

    def flaeche (self):
        return self.a * self.a

    def umfang(self):
        return self.a + self.a + self.a + self.a


q = Quadrat(3)
print(q.umfang())
print(q.info())
print(q.flaeche())