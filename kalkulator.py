a, b = input().split()
a = int(a)
b = int(b)

dodawanie = a+b
odejmowanie = a-b
mnozenie = a*b

if b == 0:
    dzielenie = "Inf"
    reszta = "NaN"
else:
    dzielenie = a // b
    reszta = a % b


print(dodawanie, end=" ")
print(odejmowanie, end=" ")
print(mnozenie, end=" ")
print(dzielenie, end=" ")
print(reszta, end=" ")