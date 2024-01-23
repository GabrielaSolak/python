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
    
class Ulamek:
    def __init__(self, l, m):
        self.licznik = l
        if m == 0:
            self.mianownik = 1
        else:
            self.mianownik = m

    def wypisz(self):
        print(f"Licznik -> {self.licznik} \nMianownik -> {self.mianownik}")

    def __str__(self):
        return f"Licznik -> {self.licznik} \nMianownik -> {self.mianownik}"   

l1 = Ulamek(2, 3)
l2 = Ulamek(4, 0)

l1.wypisz()
l2.wypisz()

print(l1)
print(l2)

class Wyraz:
    def __init__(self, w, l):
        self.wyraz = w
        self.litera = l
    def czyWyrazMaLitere(self):
        for el in self.wyraz:
            if el == self.litera:
                print("Tak")
    def __str__(self):
        return f"wyraz {self.wyraz}, litera {self.litera}"

wyraz1 = Wyraz('tekst', 'e')

wyraz1.czyWyrazMaLitere()
print(wyraz1)
