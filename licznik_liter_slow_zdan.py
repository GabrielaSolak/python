
def ilosc_liter(tekst):
    l_liter = 0
    for litera in tekst:
            if litera != " ":
                l_liter += 1
    return l_liter

def ilosc_slow(tekst):
    l_slow = 1
    for el in tekst:
            if el == " ":
                l_slow += 1
    return l_slow

def ilosc_zdan(tekst):
    l_zdan = 0
    for el in tekst:
            if el == ".":
                l_zdan += 1
    return l_zdan
while True:
    try:    
        print("Wybierz obcje:")
        print("1. Licznik liter\n2. Licznik wyrazow\n3. Licznik zadn\n4. Wszystko\n")

        obcja = int(input('> '))

        print("Podaj tekst: ")
        #tekst = input("> ")
        tekst = "To jestes przykladowy tekst. Tekst ma na celu test programu."

        if obcja == 1:
            print(f"ilosc liter w podanym tekscie wynosi -> {ilosc_liter(tekst)}\n")

        if obcja == 2: 
            print(f"ilosc wyrazow w podanym tekscie wynosi -> {ilosc_slow(tekst)}\n")

        if obcja == 3:
            print(f"liczba zdan w podanym tekscie wynosi {ilosc_zdan(tekst)}\n")

        if obcja == 4:
            print(f"ilosc liter w podanym tekscie wynosi -> {ilosc_liter(tekst)}")
            print(f"ilosc wyrazow w podanym tekscie wynosi -> {ilosc_slow(tekst)}")
            print(f"liczba zdan w podanym tekscie wynosi {ilosc_zdan(tekst)}\n") 
    except:
        print("Podano nie znana obcje!\n")
     