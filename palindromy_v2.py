
def zamianaWListe(wyraz):
    wyrazL = []
    for el in wyraz:
        wyrazL += str(el)
    return wyrazL

def odwrocenieListy(wyraz):
    odwrocnaL = []
    i = 0
    wyrazL = zamianaWListe(wyraz)
    a = len(wyrazL)
    while a > i:
        odwrocnaL.append(wyrazL[-1])
        wyrazL.pop(-1)

        i = i + 1

    return odwrocnaL

n = int(input())

if 2 <= n and n <= 200:
    i = 0
    odpowiedzi = []
    while n > i:
        a = input()

        x = zamianaWListe(a)
        y = odwrocenieListy(a)

        if x == y:
            odpowiedzi.append("TAK")
        else:
            odpowiedzi.append("NIE")

        i = i + 1

    for el in odpowiedzi:
        print(el)
