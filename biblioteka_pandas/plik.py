import pandas as pd
import random as rnd
print(pd.__version__)

dane = pd.read_csv("Pracownicy 2.csv")
#print(dane)

df = pd.DataFrame(dane)
#print(df)

#print(df[["Imię", "Nazwisko", "Płeć"]].to_string())

print(df[df['Płeć']=="M"])
print(df[df['Nazwisko']=="Baranowski"])


"""
for _ in df:
    if df[["Płeć"]].to_string == "M":
        print(df[["Płeć"]])


"""





