class Osoba:
    def __init__(self, imie='Jan', nazwisko='Nowak', pesel='00000000000', wiek=12):
        self.imie = imie
        self.nazwisko = nazwisko
        self._pesel = pesel ## protected
        self.__wiek = wiek ## private

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self._pesel} {self.__wiek}"
    
    @staticmethod #metoda statyczana
    def Haslo(haslo):
        print("Haslo: ", haslo)
    
    @classmethod #metoda klasy
    def Wiek(cls, wiek):
        if wiek < 18:
            return "nie jestes pelnoletni"
        else:
            return "jestes pelnoletni"

    def Funkcja(self):
        return f"{self.imie} {self.nazwisko} {self._pesel} self.__wiek"


osoba1 = Osoba()
osoba2 = Osoba('Adam', 'Mickiewicz', '09876567687', 48)
osoba3 = Osoba.Wiek(45)

Osoba.Haslo("1234")

print(osoba1)
print(osoba2)
print(osoba3)

Osoba.Funkcja()