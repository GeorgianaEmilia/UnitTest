from app.calc_dreptunghi import Dreptunghi

class Test_dreptunghi:
    def setup_method(self):
        print('Se executa la inceput')
        self.dreptunghi = Dreptunghi(6, 8, 'verde')
        self.listaa=[6,8,'verde']
        self.culoare_noua=[6,8,'rosu']

    def teardown_method(self):
        print('Se executa la final')

    def test_descrie(self):
        assert self.dreptunghi.descrie() == self.listaa, 'Descrierea nu functioneaza corect!'

    def test_aria(self):
        assert self.dreptunghi.aria() == 48, 'Aria nu functioneaza corect!'

    def test_permietru(self):
        assert self.dreptunghi.perimetru() == 28, 'Perimetrul nu functioneaza corect!'

    def test_schimba_culoare(self):
        self.dreptunghi.schimba_culoarea('rosu')
        assert self.dreptunghi.culoare=='rosu', 'Descrierea nu functioneaza corect!'
        assert self.dreptunghi.descrie() == self.culoare_noua, 'Descrierea nu functioneaza corect!'

    def test_init(self):
        assert self.dreptunghi.lungime == 6, 'Lungime incorect!'
        assert self.dreptunghi.latime == 8, 'Latime incorect!'
        assert self.dreptunghi.culoare == 'verde', 'Culoare incorect!'



