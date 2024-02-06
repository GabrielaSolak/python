#zwracanie indeksu najmniejszej wartosci
def Min(lista, rozmiar):
    min = lista[0]
    # index = 0
    # i = 0
    for el in lista:
        if el < min:
            min = el
            # index = i
        # i+=1
    index = 0
    for el in lista:
        if el == min:
            return index
        else:
            index+=1

liczby = [4,3,7,9,2]
print(Min(liczby, 5))

#sortowanie bombelkowe
def Bubble(lista, rozmiar):
    for j in range(rozmiar-1):
        i = 0
        for el in range(rozmiar-1-j):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
            i+=1
    return lista

print(Bubble(liczby, 5))
        
#sortowanie przez wybow
def Selection(lista, rozmiar):
    for el in range(rozmiar-1):
        Min(lista, rozmiar) 


#Sito E
zbior = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
def Sito(lista):
    l = zbior[0]
    i = 0
    for el in lista:
        if el == 




