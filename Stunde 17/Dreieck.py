from GeoForm import GeoForm

class Dreieck(GeoForm):

    def __init__(self, a, b, c, alpha, beta, gama):
        GeoForm.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.gama = gama

    def flaeche (self):
        return

    def umfang(self):
        return self.a + self.b + self.c
