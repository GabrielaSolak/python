
import random

print( "\n\n\nZasady gry w PAPIER KAMIEN NOZYCE: \n\n"
      + "    - Kamien vs Papier --> Papier wygrywa\n"
      + "    - Kamien vs Nozyce --> Kamien wygrywa\n"
      + "    - Papier vs Nozyce --> Nozyce wygrywaja\n"
)

czy_kolejna_runda = True

obcje = { 0:0, 1:"Kamien", 2:"Papier", 3:"Nozyce" }
print("\n\nPodaj nazwe uzytkownika")
nazwa_gracza = input("> ")

while czy_kolejna_runda == True:

    print("\nMozliwe wybory:\n"
          + " 1 - Kamien\n"
          + " 2 - Papier\n"
          + " 3 - Nozyce\n"
          )
    
    z = True
    while z == True:
        wybor_gracza = input("> ")
        if wybor_gracza == "1" or wybor_gracza == "2" or wybor_gracza == "3":
            wybor_gracza = int(wybor_gracza)
            z = False
            break


    wybor_komputera = random.randint(1,3)

    if wybor_gracza == wybor_komputera:
        wygrany = f"{nazwa_gracza} i komputer! MAMY REMIS!"
    elif wybor_gracza == 1 and wybor_komputera == 3:
        wygrany = nazwa_gracza
    elif wybor_gracza == 2 and wybor_komputera == 1:
        wygrany = nazwa_gracza
    elif wybor_gracza == 3 and wybor_komputera == 1:
        wygrany = nazwa_gracza
    elif wybor_gracza == 3 and wybor_komputera == 2:
        wygrany = nazwa_gracza
    else:
        wygrany = "Komputer"

    print(f"\n{nazwa_gracza} wybral ==> {obcje[wybor_gracza]}   VS   {obcje[wybor_komputera]} <== wybor komputera\n")
    print("A zatem..")
    
    print(f"WYGRYWA {wygrany}!\n\nGrasz jeszcze raz (t/n)?")
    czy_kolejna_runda_urz = input("> ")

    if czy_kolejna_runda_urz == "t":
        czy_kolejna_runda == True
    else:
        czy_kolejna_runda == False
        print("Do zobaczenia!")
        break


