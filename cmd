pip install pytest

pytest .\folder_name\
pytest .\folder_name\file_name.py

'''Obligatoriu UNIT TESTS pt ex2 - clasa Dreptunghi

Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pt toate atributele
Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

Unit tests pt toate metodele
Cum poti testa totusi schimba culoarea daca nu returneaza nimic?
Fie verificati direct valoarea atributului, fie verif ce returneaza metoda descrie()

OPTIONAL (sau dupa terminarea cursului pentru a extinde framework de unit tests)
Unit tests pt clasele Cerc, Cont si Angajat
'''