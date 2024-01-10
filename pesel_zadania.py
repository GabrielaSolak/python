while True:
  pesel = input("podaj pesel -> ")

  #czy pesel ma 11 znakow
  liczba_znakow = 0 

  for el in pesel:
      liczba_znakow += 1
  if liczba_znakow != 11:
      print("podany pesel jest nieprawidlowy (wymagane 11 cyfr)")
      break


  #czy sa same cyfry
  try:
    int(pesel)
  except:
    print("podany pesel jest nieprawidlowy (wymagane same cyfry)")
    break


  #cyfry roku, miesiąca i dnia są prawidłowe (możliwe)
  miesiac = ''
  dzien = ''
  rok = ''
  i = 0

  for el in pesel:
    if i == 0 or i == 1:
      rok += el
    elif i == 2 or i == 3:
      miesiac += el
    elif i == 4 or i == 5:
      dzien += el
    i += 1

  dzien = int(dzien)
  miesiac = int(miesiac)
  rok = int(rok)

  if dzien == 00 or dzien > 32:
    print("podany pesel jest nieprawidlowy (dzien daty)")
    break
  if miesiac == 00 or miesiac > 13 and miesiac < 20 or miesiac > 33:
    print("podany pesel jest nieprawidlowy (miesiac daty)")
    break

  #suma kontrolna
  suma_kontrolna = 0
  mno = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
  ii = 0

  for el in pesel[:-1]:
    suma_kontrolna += int(el) * mno[ii]
    ii+=1
  suma_kontrolna = str(suma_kontrolna)
  ostatnia_cyfra = suma_kontrolna[-1]
  suma_kontrolna = 10 - int(ostatnia_cyfra)
  if suma_kontrolna == 10:
    suma_kontrolna = 0

  if str(suma_kontrolna) != str(pesel[-1]):
    print("podany pesel jest nieprawidlowy (niezgodna suma kontrolna)")
    break

  print(f"pesel {pesel} jest prawidlowy")
  break






















'''
l = []

for el in pesel:

  el = int(el)

  l.append(el)



#miesiac

if l[3] > 2 or l[3] == 0:

   print("podany pesel jest nieprawidlowy")

#dzien

dd = l[4] + l[5]

if dd > 31:

  print("podany pesel jest nieprawidlowy")





#poprawnosc numeru pesel (suma kontrolna)

w = 0
l = []
i = 0

mno = [1379137913]

for el in mno:

  #w += el * l[i]

  i+=1

print(w)



ostatnia = str(w)[-1]

k = 10 - int(ostatnia)

print(k)



if k == l[-1]:

  print("suma kontrolna jest poprawna")



#losawanie

pesel_n = []

DD = input("podaj dzien (DD)")

MM = input("podaj miesiac (MM)")

RR = input("podaj rok (RRRR)")

ii = 0

for el in RR: 

  pesel_n[ii] == el #tutaj powinno byc insert (troche z cpp)

  ii+=1

for el in MM:

  pesel_n[ii] == el

  ii+=1

for el in DD:

  pesel_n[ii] == el

  ii+=1

print(pesel_n)'''