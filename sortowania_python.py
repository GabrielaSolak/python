zbior_liczb = [4, 7, 9, 12, 100, 0]

def bombelkowe(tab):
    n = len(tab)
    for i in range(n-1):
        for j in range(n-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

def przez_wybor(tab):
    n = len(tab)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
    return tab

def przez_wstawianie(tab):
    n = len(tab)
    for i in range(1, n):
        key = tab[i]
        j = i - 1
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab

#------menu--------
print("Menu:\n")
print("1. Sortowanie bąbelkowe")
print("2. Sortowanie przez wybór")
print("3. Sortowanie przez wstawianie")
print("4. Wyjście")

wyb = int(input("> "))

if wyb == 1:
    print(bombelkowe(zbior_liczb))
elif wyb == 2:
    print(przez_wybor(zbior_liczb))
elif wyb == 3:
    print(przez_wstawianie(zbior_liczb))
elif wyb == 4:
    print("Zakończenie programu.")
else:
    print("Nieprawidłowa opcja.")
