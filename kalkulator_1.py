
def kalkulator(a,operacja,b):
    if operacja == "+":
        print(f"= {a+b}")
    elif operacja == "-":
        print(f"= {a-b}")
    elif operacja == "/":
        print(f"= {a/b}")
    elif operacja == "*":
        print(f"= {a*b}")
    else:
        print("Instrukcja nieznana. Dostepne instrukcje: +, -, /, *")


while True:
    a, operacja, b = input().split() 

    try:
        a = float(a)
        b = float(b)
        kalkulator(a,operacja,b)
    except:
        print("Podane wartosci nie sa liczbami.")





