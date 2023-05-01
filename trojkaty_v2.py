
def sprawdzenie(a, b, c):
    if a + b <= c or a + c <= b or c + b <= a:
        return "NT"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        return "TP"
    elif a == b and b == c and c == a:
        return "TRB"
    elif a == b or b == c or c == a:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
            return "TPRR"
        else:
            return "TRR"
    else:
        return "T"
    
    
n = int(input())

lista = []

if n <= 200:
    y = 0
    while y < n:
        a, b, c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        lista.append(a)
        lista.append(b)
        lista.append(c)
        y += 1

z = 0
while z < n:
    print(sprawdzenie(lista[0], lista[1], lista[2]))
    lista.pop(2)
    lista.pop(1)
    lista.pop(0)
    z += 1


#    if 0 <= a and 0 <= b and 0 <= c and a <= 100 and b <= 100 and c <= 100:
#    (wywołać - wypisać) - USUNĄĆ






