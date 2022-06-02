from app.calc_cerc import Cerc

class Test_cerc:
    def setup_method(self):
        print('Se executa la inceput')
        self.cerc = Cerc(4, 'albastru')
        self.listaa=[4,'albastru']
        self.culoare_noua=[4,'bej']

    def teardown_method(self):
        print('Se executa la final')

    def test_descrie(self):
        assert self.cerc.descrie() == self.listaa, 'Descrierea nu functioneaza corect!'

    def test_aria(self):
        assert self.cerc.aria() == 50.24, 'Aria nu functioneaza corect!'

    def test_permietru(self):
        assert self.cerc.perimetru() == 25.12, 'Perimetrul nu functioneaza corect!'

    def test_schimba_culoare(self):
        self.cerc.schimba_culoarea('bej')
        assert self.cerc.culoare=='bej', 'Descrierea nu functioneaza corect!'

    def test_init(self):
        assert self.cerc.raza == 4, 'Raza incorecta!'
        assert self.cerc.culoare == 'albastru', 'Culoare incorect!'



