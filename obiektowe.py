from typing import List, Optional, Dict
import statistics

class Film:
    def __init__(self, id: int, tytul: str, gatunek: str, czas_trwania: int):
        self.id = id
        self.tytul = tytul
        self.gatunek = gatunek
        self.czas_trwania = czas_trwania
        self.__lista_ocen = []
        self.__obejrzenia = 0

    def dodaj_ocene(self, ocena: int) -> None:
        self.ocena = ocena
        self.__lista_ocen.append(ocena)

    def srednia_ocen(self) -> float:
        return sum(self.__lista_ocen) / len(self.__lista_ocen)

    def zarejestruj_obejrzenie(self) -> None:
        self.__obejrzenia += 1

    def obejrzenia(self) -> int:
        return self.__obejrzenia

    def __str__(self) -> str:
        return f"Id: {self.id}, Tytul: {self.tytul}, Gatunek: {self.gatunek}, Czas trwania: {self.czas_trwania}"

    def __repr__(self) -> str:
        return f"Film(id={self.id}, tytul={self.tytul}, gatunek={self.gatunek}, czas_trwania={self.czas_trwania})"

class Uzytkownik:
    def __init__(self, id: int, nazwa: str):
        self.id = id
        self.nazwa = nazwa
        self.__abonament = False
        self.__punkty = 0
        self.__lista_filmow = []

    def aktywuj_abonament(self) -> None:
        self.__abonament = True

    def anuluj_abonament(self) -> None:
        self.__abonament = False

    def abonament(self) -> bool:
        return self.__abonament

    def obejrzyj_film(self, film: Film, oceniaj: Optional[int] = None) -> None:
        self.__lista_filmow.append(film.id)
        film.zarejestruj_obejrzenie()
        film.dodaj_ocene(oceniaj)
        
    def dodaj_punkty(self, ile: int) -> None:
        self.__punkty += ile

    def historia_filmow(self) -> List[int]:
        return self.__lista_filmow

    def punkty(self) -> int:
        return self.__punkty

    def __repr__(self) -> str:
        return f"Uzytkownik({self.id}, {self.nazwa})"
        