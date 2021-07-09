from GeoForm import GeoForm

class gleichseitigesDreieck(GeoForm):

    def __init__(self, a, bc, alpha, betagama):
        GeoForm.__init__(self)
        self.a = a
        self.bc = bc
        self.alpha = alpha
        self.betagama = betagama

    def flaeche (self):
        return

    def umfang(self):
        return self.a + self.bc + self.bc

gK = gleichseitigesDreieck(2, 3, 80, 50)
print(gK.umfang())
print(gK.info())
