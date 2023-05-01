
def silnia(n):
    x = 1
    wynik = 1
    while x <= n:
        wynik *= x
        x += 1
    return wynik


t = int(input())

lista = []


if 5 <= t and t <= 10:
    y = 1
    while y <= t:
        n = int(input())

        lista.append(n)
        y += 1



def OddzielanieSpacja(wynik):
    if wynik < 1000:
        return wynik
    else:
        L = []
        wynik = str(wynik)
        for el in wynik:
            L.append(el)
        
        IlEl = len(L)

        Lk = []


        if IlEl % 3 == 1:
            Lk.append(L[0])
            L.pop(0)
            Lk.append(" ")
            
            for el in L:
                Lk.append(L[0])
                Lk.append(L[1])
                Lk.append(L[2])
                Lk.append(" ")
                L.pop(2)
                L.pop(1)
                L.pop(0)


        elif IlEl % 3 == 2:
            Lk.append(L[0])
            Lk.append(L[1])
            L.pop(1)
            L.pop(0)
            Lk.append(" ")

            for el in L:
                Lk.append(L[0])
                Lk.append(L[1])
                Lk.append(L[2])
                Lk.append(" ")
                L.pop(2)
                L.pop(1)
                L.pop(0)


        elif IlEl % 3 == 0:
            for el in L:
                Lk.append(L[0])
                Lk.append(L[1])
                Lk.append(L[2])
                Lk.append(" ")
                L.pop(2)
                L.pop(1)
                L.pop(0)

        Lk.pop(-1)
        wynik = ""
        #zamiana listy na tekst:
        for el in Lk:
            #el = str(el)
            wynik += str(el)

        return wynik




for el in lista:
    wynik = silnia(el)
    print(OddzielanieSpacja(wynik))





#-----------------------------------------------------------

















































'''
def zmianaKolejnosci(x):
    # x - duża liczba
    x = str(x)
    
    osobneElementy = []

    for el in x:
        osobneElementy.append(el)
    
    odwrocone = []

    IlEl = len(osobneElementy)
    y = 0

    while IlEl > y:
        odwrocone.append(osobneElementy[-1])
        osobneElementy.pop(-1)
        y = y + 1


    # dodawanie spacji

    zeSpacjaOdwrot = []

    




    return 
















# dla rozdzielania elementów - DZIAŁA
for el in lista:
    wynik = silnia(el)
    print(f"{int(wynik):_}".replace("_"," "))

'''












'''
for el in lista:
    wynik = silnia(el)


    if wynik > 999:

        wynik = str(wynik)

        dlugosc = len(wynik)
        listaTekst = []


        for i in range(0,dlugosc):
            # print(wynik[i], end=' ')
            listaTekst.append(wynik[i])


        if dlugosc % 3 == 0:
            c = 0
            while c < dlugosc // 3:
                listaTekstSpacje = listaTekst[-3] + listaTekst[-2] + listaTekst[-1] + " - "
                listaTekst.pop(-3)
                listaTekst.pop(-2)
                listaTekst.pop(-1)
                c += 1
            print(listaTekstSpacje)




        elif dlugosc % 3 == 1:
            v = 0
            while v < dlugosc // 3:
                listaTekstSpacje = listaTekst[-3] + listaTekst[-2] + listaTekst[-1] + " - "
                listaTekst.pop(-3)
                listaTekst.pop(-2)
                listaTekst.pop(-1)
                v += 1
            print(listaTekstSpacje)


        elif dlugosc % 3 == 2:
            z = 0
            while z < dlugosc // 3:
                listaTekstSpacje = listaTekst[-3] + listaTekst[-2] + listaTekst[-1] + " - "
                listaTekst.pop(-3)
                listaTekst.pop(-2)
                listaTekst.pop(-1)
                z += 1
            print(listaTekstSpacje)


    else:
        print(wynik)

    print(f"{int(wynik):_}".replace("_"," "))
    





'''


