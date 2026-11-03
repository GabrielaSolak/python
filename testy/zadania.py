#zad_1
def ile_znakow(tekst):
    slownik_wystapien = {}
    for litera in tekst:
        if litera in slownik_wystapien:
            slownik_wystapien[litera] += 1
        else:
            slownik_wystapien[litera] = 1
    return slownik_wystapien

    
#zad_2
def usuwanie_duplikatow_z_listy(lista):
    unikalne = []
    for el in lista:
        if el not in unikalne:
            unikalne.append(el)
    return unikalne

#zad_3
def ile_dni(miesiac, rok):
    if miesiac < 1 or miesiac > 12:
        return -1
    elif miesiac % 2 == 1:
        return 31
    elif miesiac == 2 and rok % 400 == 0 or (rok % 4 == 0 and rok % 100 != 0):
        return 29
    elif miesiac == 2:
        return 28
    elif miesiac % 2 == 0:
        return 30

#zad_4
def reszta(kwota_zaplacona, cena):
    reszta = kwota_zaplacona - cena
    return reszta

#ile_znakow("tekst")
#lista = [1, 2, 1, 5, 6]
#print(usuwanie_duplikatow_z_listy(lista))
#print(ile_dni(3, 2027))
