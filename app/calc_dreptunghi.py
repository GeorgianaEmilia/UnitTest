class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        self.lista=[self.lungime, self.latime, self.culoare]
        return self.lista

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2*(self.lungime + self.latime)

    def schimba_culoarea(self,noua_culoare):
        self.culoare = noua_culoare


    '''
Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pt toate atributele
Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. 
Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''
