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

#ile srednio zarabiają kobiety

pln = []
for el in df['Zarobki']:
    pln.append(float((el[:-4]).replace(" ", "")))

df['pln'] = pln
del df['Zarobki']

df['usd'] = df['pln']/3.98
print(df[['usd','pln']][df['usd']>2000].mean())
