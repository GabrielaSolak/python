class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = 17

    def wyswietl(self):
        print(self.imie, self.nazwisko)


lista = []

lista.append(Osoba('Jan', 'Nowak'))
lista.append(Osoba('Yfjda;iej', 'JKL:F'))

for o in lista:
    o.wyswietl()


class Ksiazka:
    def __init__(self, tytul, imie_autora, nazwisko_autora, liczba_stron):
        self.tytul = tytul
        self.imie_autora = imie_autora
        self.nazwisko_autora = nazwisko_autora
        self.liczba_stron = liczba_stron
    def tekst(self):
        print(f"Autorem ksia")
    
