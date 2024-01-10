def sumaKontrolna(pesel):
    #suma kontrolna
    suma_kontrolna = 0
    mno = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    ii = 0

    for el in pesel:
        suma_kontrolna += int(el) * mno[ii]
        ii+=1
    suma_kontrolna = str(suma_kontrolna)
    ostatnia_cyfra = suma_kontrolna[-1]
    suma_kontrolna = 10 - int(ostatnia_cyfra)
    if suma_kontrolna == 10:
        suma_kontrolna = 0

    return suma_kontrolna

# RR MM DD PPP X K
while True:
    rok = input("Podaj rok urodzenia -> ")
    mm = input("Podaj miesiac urodzenia -> ")
    dd = input("Podaj dzien urodzenia -> ")
    x = input("Podaj plec (k/m) -> ")

    if int(rok) > 1900 and int(rok) < 2025 and int(mm) > 0 and int(mm) < 13 and int(dd) > 0 and int(dd) < 32 and x == 'k' or x == 'm':
        break

rr = rok[-2] + rok[-1]
if int(rok) > 1999:
    mm = int(mm) + 20
ppp = 0
if x == 'k':
    x = 0
else:
    x = 1

pesel = ''


pesel += rr
pesel += str(mm)
pesel += dd

print("Możliwe pesele:")
while ppp < 999:
    while x < 10:
        if ppp < 10:
            m_pesel = pesel + '00' + str(ppp) + str(x)
            k = sumaKontrolna(m_pesel)
            print(f"{pesel} 00{ppp} {x} {k}")
        elif ppp < 100:
            m_pesel = pesel + '0' + str(ppp) + str(x)
            k = sumaKontrolna(m_pesel)
            print(f"{pesel} 0{ppp} {x} {k}")
        else:
            m_pesel = pesel + str(ppp) + str(x)
            k = sumaKontrolna(m_pesel)
            print(f"{pesel} {ppp} {x} {k}")
        x += 2
    ppp += 1
    x = 0