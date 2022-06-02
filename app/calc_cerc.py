class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie(self):
        self.lista=[self.raza,self.culoare]
        return self.lista

    def aria(self):
        return 3.14*(self.raza*self.raza)

    def perimetru(self):
        return 2*(3.14 * self.raza)

    def schimba_culoarea(self,noua_culoare):
        self.culoare = noua_culoare